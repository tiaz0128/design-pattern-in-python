from abc import ABC, abstractmethod
from typing import override

from factory.factory_method.pizza import (
    ChicagoStyleCheesePizza,
    NYStyleCheesePizza,
    PizzaType,
)


class MethodFactory(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


class NYPizzaFactory(MethodFactory):
    @override
    def create_pizza(self, pizza_type):
        match pizza_type:
            case PizzaType.CHEESE:
                return NYStyleCheesePizza()


class ChicagoPizzaFactory(MethodFactory):
    @override
    def create_pizza(self, pizza_type):
        self.cut_rectangle()

        match pizza_type:
            case PizzaType.CHEESE:
                return ChicagoStyleCheesePizza()

    def cut_rectangle(self):
        print("시카고 피자는 모양이 네모납니다.")
