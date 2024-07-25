from abc import ABC


class Pizza(ABC):
    name = "핏자"


class CheesePizza(Pizza):
    name = "치즈 핏자"


class ClamPizza(Pizza):
    name = "해산물 핏자"
