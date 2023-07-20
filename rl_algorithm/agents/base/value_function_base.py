from abc import ABCMeta, abstractmethod

class ValueFunctionBase(metaclass=ABCMeta):
    def __init__(cls, value_function):
        cls.set_value_function(value_function)

    @abstractmethod
    def get_value(self, state):
        pass
    
    @abstractmethod
    def set_value_function(cls, value_function, key):
        pass
    
    @abstractmethod
    def get_value_function(cls, key):
        pass

class ValueFuncSingleton(ValueFunctionBase):
    _instance = None
    _value_functions = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def set_value_function(cls, value_function, key="default"):
        cls._value_functions[key] = value_function
    
    def get_value_function(cls, key="default"):
        return cls._value_functions[key]