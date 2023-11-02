from abc import ABC, abstractmethod

from ingredient import (
    Dough,
    ThinCrustDough,
    ThickCrustDough,
    Cheese,
    ReggianoCheese,
    MozzarellaCheese,
)


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()
