from enum import StrEnum


class Pizza:
    name = "피자"


class NYStyleCheesePizza(Pizza):
    name = "뉴욕 치즈 핏자"


class ChicagoStyleCheesePizza(Pizza):
    name = "시카고 치즈 핏자"


class PizzaType(StrEnum):
    CHEESE = "cheese"
    CLAM = "clam"
