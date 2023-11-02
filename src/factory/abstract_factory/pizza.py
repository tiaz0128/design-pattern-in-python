from abc import ABC, abstractmethod
from enum import Enum

from pizza_ingredient_factory import PizzaIngredientFactory


class Pizza(ABC):
    def __init__(self) -> None:
        self._name: str = ""

        self.dough: str = ""
        self.cheese: str = ""

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print("175도에서 25분 간 굽기")

    def cut(self) -> None:
        print("피자 사선으로 자르기")

    def box(self) -> None:
        print("상장 피자 담기")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print(f"준비 중: {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.cheese = self.ingredient_factory.create_cheese()


class PizzaType(Enum):
    CHEESE = "cheese"
