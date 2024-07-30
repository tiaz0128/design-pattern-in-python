from abc import ABC
from enum import StrEnum


class Pizza(ABC):
    name = "피자"


class NYStyleCheesePizza(Pizza):
    name = "뉴욕 치즈 핏자"


class ChicagoStyleCheesePizza(Pizza):
    name = "시카고 치즈 핏자"


class PizzaType(StrEnum):
    CHEESE = "cheese"
