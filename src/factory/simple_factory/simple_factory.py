from enum import StrEnum

from factory.simple_factory.pizza import CheesePizza, ClamPizza


class PizzaType(StrEnum):
    CHEESE_PIZZA = "cheese pizza"
    CLAM_PIZZA = "clam pizza"


class SimplePizzaFactory:
    def create_pizza(self, pizza_type: PizzaType):
        match pizza_type:
            case PizzaType.CHEESE_PIZZA:
                return CheesePizza()
            case PizzaType.CLAM_PIZZA:
                return ClamPizza()
