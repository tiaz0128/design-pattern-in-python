from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ThinCrustDough(Dough):
    def __str__(self) -> str:
        return "ThinCrustDough"


class ThickCrustDough(Dough):
    def __str__(self) -> str:
        return "ThickCrustDough"


class Cheese(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ReggianoCheese(Cheese):
    def __str__(self) -> str:
        return "ReggianoCheese"


class MozzarellaCheese(Cheese):
    def __str__(self) -> str:
        return "MozzarellaCheese"
