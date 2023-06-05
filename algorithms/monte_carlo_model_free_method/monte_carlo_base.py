import sys
import numpy as np
from collections import defaultdict

class MonteCarloBase:
    def __init__(self, number_of_action):
        self.counter = defaultdict(lambda: np.zeros(number_of_action))
        self.sum_of_returns = defaultdict(lambda: np.zeros(number_of_action))
        self.value_estimation = defaultdict(lambda: np.zeros(number_of_action))

    def mc_prediction_q(env, num_episodes, generate_episode, gamma=1.0):
        # initialize empty dictionaries of arrays
        returns_sum = defaultdict(lambda: np.zeros(env.action_space.n))
        N = defaultdict(lambda: np.zeros(env.action_space.n))
        Q = defaultdict(lambda: np.zeros(env.action_space.n))
        # loop over episodes
        for i_episode in range(1, num_episodes+1):
            # monitor progress
            if i_episode % 1000 == 0:
                print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
                sys.stdout.flush()
            # generate an episode
            episode = generate_episode(env)
            # obtain the states, actions, and rewards
            states, actions, rewards = zip(*episode)
            # prepare for discounting
            discounts = np.array([gamma**i for i in range(len(rewards)+1)])
            # update the sum of the returns, number of visits, and action-value 
            # function estimates for each state-action pair in the episode
            for i, state in enumerate(states):
                returns_sum[state][actions[i]] += sum(rewards[i:]*discounts[:-(1+i)])
                N[state][actions[i]] += 1.0
                Q[state][actions[i]] = returns_sum[state][actions[i]] / N[state][actions[i]]
        return Q