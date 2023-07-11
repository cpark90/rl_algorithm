import abc

class PolicySingleton:
    _instance = None
    _model_class = None
    _value_function_class = None
    _policies = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def set_policy(cls, policy, key="default"):
        cls._policies[key] = policy
    
    def get_policy(cls, key="default"):
        return cls._policies[key]

    def get_model_class(cls):
        return cls._model_class
    
    def get_value_function_class(cls):
        return cls._value_function_class

class PolicyBase(PolicySingleton):
    def __init__(cls, policy, model_class, value_function_class):
        cls.set_policy(policy)
        cls._model_class = model_class
        cls._value_function_class = value_function_class

    @abc.abstractmethod
    def act(self, current_state):
        pass
