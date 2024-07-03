class Singleton:
    _instance = None

    def __new__(cls) -> None:

        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance
