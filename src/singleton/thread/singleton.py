from singleton.thread.meta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass
