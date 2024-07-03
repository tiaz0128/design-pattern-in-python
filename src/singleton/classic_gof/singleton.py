class Singleton:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError("Call instance() method")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)

        return cls._instance
