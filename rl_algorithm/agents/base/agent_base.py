class AgentBase:
    def __init__(self, state_estimation, reward_estimation, policy_class, model_class, value_function_class):
        self.episodes = []
        self.current_episode = []
        self.current_mdp_pair = {}
        self.current_state = None

        self.state_estimation = state_estimation
        self.reward_estimation = reward_estimation
        
        self.policy_class = policy_class
        self.model_class = model_class
        self.value_function_class = value_function_class
    
    def start_new_episode(self, state_feature):
        if self.current_episode:
            self.append_episode()
        self.current_state = self.state_estimation(state_feature)

    def observe(self, observation):
        state = self.state_estimation(observation["state"])
        reward = self.reward_estimation(observation["reward"])
        self.current_mdp_pair["next_state"] = state
        self.current_mdp_pair["reward"] = reward
        self.current_state = state
        self.current_episode.append(self.current_mdp_pair)
    
    def act(self):
        self.current_mdp_pair = {}
        action = self.policy_class.act(self.current_state)
        self.current_mdp_pair["state"] = self.current_state
        self.current_mdp_pair["action"] = action
        return action
    
    def append_episode(self):
        self.episodes.append(self.current_episode)
        self.current_episode = []

    def update_value_function(self):
        raise NotImplementedError

    def update_model(self):
        raise NotImplementedError