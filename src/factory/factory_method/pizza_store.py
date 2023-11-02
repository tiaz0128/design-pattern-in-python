from abc import ABC, abstractmethod
from pizza import ChicagoStyleCheesePizza, NYStyleCheesePizza, PizzaType


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
        match pizza_type:
            case PizzaType.CHEESE:
                return NYStyleCheesePizza()


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        match pizza_type:
            case PizzaType.CHEESE:
                return ChicagoStyleCheesePizza()

    def cut(self):
        print("네모로 짜름")
