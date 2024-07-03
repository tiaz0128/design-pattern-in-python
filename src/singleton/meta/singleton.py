from singleton.meta.singleton_meta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    _instance = None

    def some_business_logic(self):
        pass
