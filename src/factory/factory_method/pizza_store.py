import logging

from factory.factory_method.method_factory import MethodFactory
from factory.factory_method.pizza import Pizza, PizzaType


class PizzaStore:
    def __init__(self, factory: MethodFactory) -> None:
        self.factory = factory

    def order(self, pizza_type: PizzaType) -> Pizza:
        pizza = self.factory.create_pizza(pizza_type)

        logging.info(f"{pizza.name}를 주문하셨습니다.")

        return pizza
