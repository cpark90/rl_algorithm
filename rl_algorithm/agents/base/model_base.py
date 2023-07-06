class ModelMeta(type):
    _models = {}

    def __init__(cls, model):
        cls.set_model(model)
    
    def set_model(cls, model, key="default"):
        cls._models[key] = model
    
    def get_model(cls, key="default"):
        return cls._models[key]


class ModelBase(metaclass=ModelMeta):
    def transition(self, state, action):
        raise NotImplementedError
