from enum import Enum


class Pizza:
    name = "피자"

    def bake(self):
        print(f"{self.name} 빵을 굽자")

    def cut(self):
        print("세모로 짜름")

    def box(self):
        print("피자를 담자")


class NYStyleCheesePizza(Pizza):
    name = "뉴욕 치즈 핏자"


class ChicagoStyleCheesePizza(Pizza):
    name = "시카고 치즈 핏자"


class PizzaType(Enum):
    CHEESE = "cheese"
