import abc

class ModelSingleton:
    _instance = None
    _models = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def set_model(cls, model, key="default"):
        cls._models[key] = model
    
    def get_model(cls, key="default"):
        return cls._models[key]


class ModelBase(ModelSingleton):
    def __init__(cls, model):
        cls.set_model(model)

    @abc.abstractmethod
    def transition(self, state, action):
        pass
