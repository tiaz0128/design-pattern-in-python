from singleton.eager.meta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass
