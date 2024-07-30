import logging
from factory.simple_factory.pizza import Pizza
from factory.simple_factory.simple_factory import PizzaType, SimplePizzaFactory


class PizzaStore:
    def __init__(self) -> None:
        self.factory = SimplePizzaFactory()

    def order(self, pizza_type: PizzaType) -> Pizza:
        pizza = self.factory.make_pizza(pizza_type)

        logging.info(f"{pizza.name}를 주문하셨습니다.")

        return pizza
