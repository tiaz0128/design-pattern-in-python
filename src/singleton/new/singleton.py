from typing import Self


class Singleton:
    _instance = None

    def __new__(cls) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance
