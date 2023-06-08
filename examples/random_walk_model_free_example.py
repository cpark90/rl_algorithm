import gymnasium as gym
import numpy as np
import envs
from algorithms import MonteCarloMethod

env = gym.make('random_walk-v0', n_actions=1)
first_visit_monte_carlo_method = MonteCarloMethod(env.action_space.n, gamma=1)
every_visit_monte_carlo_method = MonteCarloMethod(env.action_space.n, gamma=1)
num_episodes = 100

for i in range(num_episodes):
    state_feature = env.reset()
    print ("starting new episode : " + str(i))
    episode = []

    done = False
    while True:
        action = np.random.randint(env.action_space.n)
        next_state_feature, reward, done, _ = env.step(action)
        episode.append([state_feature, action, reward])
        # env.render()
        state_feature = next_state_feature
        if done:
            break
    first_visit_monte_carlo_method.first_visit_prediction(episode)
    every_visit_monte_carlo_method.every_visit_prediction(episode)