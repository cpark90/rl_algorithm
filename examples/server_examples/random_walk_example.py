import gymnasium as gym
import numpy as np
import envs
from rl_algorithm.algorithms import MonteCarloMethod, TemporalDifferenceMethod
from collections import OrderedDict

import plotly.graph_objs as go
import plotly.offline as py

n_states = 5
env = gym.make('random_walk-v0', n_states=n_states, n_actions=1)

num_episodes = 5000

mc_method_average = MonteCarloMethod(number_of_action=env.action_space.n, first_visit=False, online=False, gamma=1.0, alpha=0.0, initialize_method="0_5")
mc_method_0_01 = MonteCarloMethod(number_of_action=env.action_space.n, first_visit=False, online=False, gamma=1.0, alpha=0.01, initialize_method="0_5")
mc_method_0_01_f = MonteCarloMethod(number_of_action=env.action_space.n, first_visit=True, online=False, gamma=1.0, alpha=0.01, initialize_method="0_5")
td_method_0_15 = TemporalDifferenceMethod(number_of_action=env.action_space.n, n_step=1, lambda_=0.0, gamma=1.0, alpha=0.15, initialize_method="0_5")
td_method_0_05 = TemporalDifferenceMethod(number_of_action=env.action_space.n, n_step=1, lambda_=0.0, gamma=1.0, alpha=0.05, initialize_method="0_5")


data_episode = {}
for i in range(num_episodes):
    state = env.reset()
    total_reward = 0
    done = False
    episode = []
    while True:
        action = np.random.randint(env.action_space.n)
        next_state, reward, done, _ = env.step(action)
        episode.append([state, action, reward])
        # env.render()
        state = next_state
        if done:
            break
    mc_method_average.averaging(episode)
    
    mc_method_0_01.incremental(episode)
    mc_method_0_01_f.incremental(episode)
    td_method_0_15.offline(episode)
    td_method_0_05.offline(episode)

    if i < 100:
        data_alpha = {}

        mc_q_0_01 = mc_method_0_01.get_value_function(n_states=n_states)
        mc_y_0_01 = np.squeeze(np.array(tuple(mc_q_0_01[key] for key in sorted(mc_q_0_01))))
        data_alpha["mc_y_0_01"] = mc_y_0_01

        mc_q_0_01_f = mc_method_0_01_f.get_value_function(n_states=n_states)
        mc_y_0_01_f = np.squeeze(np.array(tuple(mc_q_0_01_f[key] for key in sorted(mc_q_0_01_f))))
        data_alpha["mc_y_0_01_f"] = mc_y_0_01_f

        td_q_0_15 = td_method_0_15.get_value_function(n_states=n_states)
        td_y_0_15 = np.squeeze(np.array(tuple(td_q_0_15[key] for key in sorted(td_q_0_15))))
        data_alpha["td_y_0_15"] = td_y_0_15

        td_q_0_05 = td_method_0_05.get_value_function(n_states=n_states)
        td_y_0_05 = np.squeeze(np.array(tuple(td_q_0_05[key] for key in sorted(td_q_0_05))))
        data_alpha["td_y_0_05"] = td_y_0_05

        data_episode[i] = data_alpha

# make graph
mc_q_average = mc_method_average.get_value_function(n_states=n_states)
mc_y_average = np.squeeze(np.array(tuple(mc_q_average[key] for key in sorted(mc_q_average))))


x = np.linspace(start=1, stop=len(data_episode), num=len(data_episode))

data = {}
for key in data_episode.keys():
    data_alpha = data_episode[key]
    for alpha in data_alpha.keys():
        if alpha not in data.keys():
            data[alpha] = []
        data[alpha].append(np.sqrt(np.mean((data_alpha[alpha] - mc_y_average)**2)))

data_graph = []
for alpha in data.keys():
    data_graph.append(go.Scatter(x=x, y=data[alpha], name='{}'.format(alpha)))

py.plot(data_graph)