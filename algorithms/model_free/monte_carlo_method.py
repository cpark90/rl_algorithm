import sys
import numpy as np

from copy import copy
from collections import defaultdict

class MonteCarloMethod:
    def __init__(self, number_of_action, first_visit=False, online=False, gamma=1.0, alpha=0, initialize_method="zeros"):
        self.number_of_action = number_of_action
        self.counter = defaultdict(lambda: np.zeros(number_of_action))
        self.sum_of_returns = defaultdict(lambda: np.zeros(number_of_action))
        self.value_estimation = self._value_function_initialize(number_of_action=number_of_action, method=initialize_method)
        self.value_estimation_backup = None
        self.first_visit = first_visit
        self.online = online
        self.gamma = gamma
        self.alpha = alpha

    def _value_function_initialize(self, number_of_action, method="zeros"):
        initialized_value_function = None
        if method == "zeros":
            initialized_value_function = defaultdict(lambda: np.zeros(number_of_action))
        elif method == "ones":
            initialized_value_function = defaultdict(lambda: np.ones(number_of_action))
        elif method == "0_5":
            initialized_value_function = defaultdict(lambda: np.ones(number_of_action) * 0.5)
        return initialized_value_function
    
    def averaging(self, episode):
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([self.gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode

        if self.first_visit:
            updated = defaultdict(lambda: np.zeros(self.number_of_action))

        for i, state in enumerate(states):
            # check first visit
            if self.first_visit:
                if updated[state][actions[i]] == 1:
                    continue
                else:
                    updated[state][actions[i]] = 1

            # increment counter
            self.counter[state][actions[i]] += 1.0
            
            # calculate sum of returns
            self.sum_of_returns[state][actions[i]] += sum(rewards[i:] * discounts[:-(1+i)])

            # update value_function
            self.value_estimation[state][actions[i]] = self.sum_of_returns[state][actions[i]] / self.counter[state][actions[i]]

    def incremental(self, episode):
        # update backup
        if self.online:
            self.value_estimation_backup = self.value_estimation
        else:    
            self.value_estimation_backup = copy(self.value_estimation)

        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([self.gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode

        if self.first_visit:
            updated = defaultdict(lambda: np.zeros(self.number_of_action))

        for i, state in enumerate(states):
            # check first visit
            if self.first_visit:
                if updated[state][actions[i]] == 1:
                    continue
                else:
                    updated[state][actions[i]] = 1

            # increment counter
            self.counter[state][actions[i]] += 1.0
            
            # calculate target
            target = sum(rewards[i:] * discounts[:-(1+i)])

            # calculate error
            error = target - self.value_estimation_backup[state][actions[i]]

            # update value_function
            if self.alpha == 0:
                self.value_estimation[state][actions[i]] = self.value_estimation_backup[state][actions[i]] + error / self.counter[state][actions[i]]
            else:
                self.value_estimation[state][actions[i]] = self.value_estimation_backup[state][actions[i]] + error * self.alpha
        
    
    def get_value_function(self, n_states=None):
        if n_states is not None:
            for i_s in range(n_states):
                i_s += 1
                for i_a in range(self.number_of_action):
                    if i_s not in self.value_estimation.keys():
                        self.value_estimation[i_s][i_a] = np.array([0])

        return self.value_estimation