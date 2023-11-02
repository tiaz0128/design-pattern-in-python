from enum import Enum

from pizza import CheesePizza, ClamPizza


class PizzaType(Enum):
    CHEESE_PIZZA = "cheese pizza"
    CLAM_PIZZA = "clam pizza"


class SimplePizzaFactory:
    def create_pizza(self, pizza_type: PizzaType):
        match pizza_type:
            case PizzaType.CHEESE_PIZZA:
                return CheesePizza()
            case PizzaType.CLAM_PIZZA:
                return ClamPizza()
