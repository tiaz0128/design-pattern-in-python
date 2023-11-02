from abc import ABC, abstractmethod

from pizza_ingredient_factory import (
    NYPizzaIngredientFactory,
    ChicagoPizzaIngredientFactory,
)
from pizza import CheesePizza, PizzaType


class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = NYPizzaIngredientFactory()

        match pizza_type:
            case PizzaType.CHEESE:
                pizza = CheesePizza(ingredient_factory)
                return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        ingredient_factory = ChicagoPizzaIngredientFactory()

        match pizza_type:
            case PizzaType.CHEESE:
                pizza = CheesePizza(ingredient_factory)
                return pizza
