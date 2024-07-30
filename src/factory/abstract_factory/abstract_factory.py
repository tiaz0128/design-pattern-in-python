from abc import ABC, abstractmethod

from factory.abstract_factory.ingredient import (
    Cheese,
    Dough,
    MozzarellaCheese,
    ReggianoCheese,
    ThickCrustDough,
    ThinCrustDough,
)


class AbstractFactory(ABC):
    name = "공장"

    @abstractmethod
    def make_dough(self) -> Dough:
        pass

    @abstractmethod
    def make_cheese(self) -> Cheese:
        pass


class NYPizzaFactory(AbstractFactory):
    name = "뉴욕 공장"

    def make_dough(self) -> Dough:
        return ThinCrustDough()

    def make_cheese(self) -> Cheese:
        return ReggianoCheese()


class ChicagoPizzaFactory(AbstractFactory):
    name = "시카고 공장"

    def make_dough(self) -> Dough:
        return ThickCrustDough()

    def make_cheese(self) -> Cheese:
        return MozzarellaCheese()
