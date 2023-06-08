class PolicyMeta(type):
    _model_class = None
    _value_function_class = None
    _policies = {}

    def __init__(cls, policy, model_class, value_function_class):
        cls.set_policy(policy)
        cls._model_class = model
        cls._value_function_class = value_function_class
    
    def set_policy(cls, policy, key="default"):
        cls._policies[key] = policy
    
    def get_policy(cls, key="default"):
        return cls._policies[key]

    def get_model_class(cls):
        return cls._model_class
    
    def get_value_function_class(cls):
        return cls._value_function_class

class PolicyBase(metaclass=PolicyMeta):
    def act(self, current_state):
        raise NotImplementedError
