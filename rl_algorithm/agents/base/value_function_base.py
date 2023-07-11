import abc

class ValueFuncSingleton:
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


class ValueFunctionBase(ValueFuncSingleton):
    def __init__(cls, value_function):
        cls.set_value_function(value_function)

    @abc.abstractmethod
    def get_value(self, state):
        pass