from abc import ABCMeta, abstractmethod

class ModelBase(metaclass=ABCMeta):
    @abstractmethod
    def set_model(self, model, key):
        pass

    @abstractmethod
    def get_model(self, key):
        pass

    @abstractmethod
    def transition(self, state, action):
        pass

class ModelSingleton(ModelBase):
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

class ModelRedis(ModelBase):
    def __init__(cls, redis_module):
        cls.r = redis_module
    
    def set_model(cls, model, key="default"):
        r.set(key, model)
    
    def get_model(cls, key="default"):
        return cls.r.get(key)
    
    def close(cls):
        cls.r.close()

if __name__ == "__main__":
    a = ModelSingleton()
    b = ModelSingleton()
    a.set_model("hello")
    print(b.get_model())