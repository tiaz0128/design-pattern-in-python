from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass

    @abstractmethod
    def recipe(self) -> list[str]:
        pass
