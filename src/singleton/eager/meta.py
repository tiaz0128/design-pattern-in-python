import logging


class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, attrs):
        logging.info("metaclass __init__")

        super().__init__(name, bases, attrs)

        instance = super().__call__()
        cls._instances[cls] = instance

    def __call__(cls, *args, **kwargs):
        logging.info("metaclass __call__")

        return cls._instances[cls]
