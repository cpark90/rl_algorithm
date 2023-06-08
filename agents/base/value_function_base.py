class ValueFunctionMeta(type):
    _value_functions = {}

    def __init__(cls, value_function):
        cls.set_value_function(value_function)
    
    def set_value_function(cls, value_function, key="default"):
        cls._value_functions[key] = value_function
    
    def get_value_function(cls, key="default"):
        return cls._value_functions[key]


class ValueFunctionBase(metaclass=ValueFunctionMeta):
    def get_value(self, state):
        raise NotImplementedError