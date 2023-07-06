import sys
import numpy as np
from copy import copy
from collections import defaultdict

class TemporalDifferenceMethod:
    def __init__(self, number_of_action, n_step=1, lambda_=0.0, gamma=1.0, alpha=0.0, initialize_method="zeros"):
        self.number_of_action = number_of_action
        self.value_estimation = self._value_function_initialize(number_of_action=number_of_action, method=initialize_method)
        self.value_estimation_backup = self.value_estimation
        self.n_step = n_step
        self.lambda_ = lambda_
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

    def offline(self, episode):
        # update backup
        self.value_estimation_backup = copy(self.value_estimation)

        states, actions, rewards = zip(*episode)
        # prepare for discounting

        for i, state in enumerate(states):
            final_step = i + self.n_step
            if final_step > len(states) - 1:
                next_state_and_action = None
            else:
                next_state_and_action = {"state":states[final_step], "action":actions[final_step]}
            self.online(state=state, action=actions[i], rewards=rewards[i:i+self.n_step], next_state_and_action=next_state_and_action)

    def online(self, state, action, rewards, next_state_and_action):
        discounts = np.array([self.gamma**i for i in range(len(rewards)+1)])
        
        # calculate target
        target = sum(rewards[:] * discounts[:-1])
        if next_state_and_action is not None:
            target += self.value_estimation[next_state_and_action["state"]][next_state_and_action["action"]] * discounts[-1]
        
        # calculate error
        error = target - self.value_estimation_backup[state][action]

        # update value_function
        self.value_estimation[state][action] = self.value_estimation_backup[state][action] + error * self.alpha

    def get_value_function(self, n_states=None):
        if n_states is not None:
            for i_s in range(n_states):
                i_s += 1
                for i_a in range(self.number_of_action):
                    if i_s not in self.value_estimation.keys():
                        self.value_estimation[i_s][i_a] = np.array([0])

        return self.value_estimation