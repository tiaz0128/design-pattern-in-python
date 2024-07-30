from abc import ABC, abstractmethod
from typing import override


class Dough(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ThinCrustDough(Dough):
    @override
    def __str__(self) -> str:
        return "ThinCrustDough"


class ThickCrustDough(Dough):
    @override
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
