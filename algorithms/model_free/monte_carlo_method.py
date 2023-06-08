import sys
import numpy as np
from collections import defaultdict

class MonteCarloMethod:
    def __init__(self, number_of_state_and_action, gamma=1.0):
        self.number_of_state_and_action = number_of_state_and_action
        self.counter = defaultdict(lambda: np.zeros(number_of_state_and_action))
        self.sum_of_returns = defaultdict(lambda: np.zeros(number_of_state_and_action))
        self.value_estimation = defaultdict(lambda: np.zeros(number_of_state_and_action))
        self.gamma = gamma

    def every_visit_prediction(self, episode):
        # obtain the states, actions, and rewards
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([self.gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode
        for i, state in enumerate(states):
            self.sum_of_returns[state][actions[i]] += sum(rewards[i:]*discounts[:-(1+i)])
            self.counter[state][actions[i]] += 1.0
            self.value_estimation[state][actions[i]] = self.sum_of_returns[state][actions[i]] / self.counter[state][actions[i]]
    
    def first_visit_prediction(self, episode):
        # obtain the states, actions, and rewards
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([self.gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode
        updated = defaultdict(lambda: np.zeros(self.number_of_state_and_action))
        for i, state in enumerate(states):
            if updated[state][actions[i]] == 1:
                continue
            else:
                updated[state][actions[i]] = 1
            self.sum_of_returns[state][actions[i]] += sum(rewards[i:]*discounts[:-(1+i)])
            self.counter[state][actions[i]] += 1.0
            self.value_estimation[state][actions[i]] = self.sum_of_returns[state][actions[i]] / self.counter[state][actions[i]]
    
    def get_value_function(self):
        return self.value_estimation