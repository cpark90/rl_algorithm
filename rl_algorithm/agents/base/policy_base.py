from abc import ABCMeta, abstractmethod

class PolicyBase(metaclass=ABCMeta):
    @abstractmethod
    def act(cls, current_state):
        pass
    
    @abstractmethod
    def set_policy(cls, policy):
        pass

    @abstractmethod
    def set_model_class(cls, model_class):
        pass
    
    @abstractmethod
    def set_value_function_class(cls, value_function_class):
        pass

class PolicySingleton(PolicyBase):
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

    def set_model_class(cls, model_class):
        cls._model_class = model_class
    
    def set_value_function_class(cls, value_function_class):
        cls._value_function_class = value_function_class
    
    def get_policy(cls, key="default"):
        return cls._policies[key]

    def get_model_class(cls):
        return cls._model_class
    
    def get_value_function_class(cls):
        return cls._value_function_class