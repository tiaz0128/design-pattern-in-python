from abc import ABC


class Pizza(ABC):
    name = "핏자"

    @classmethod
    def prepare(cls):
        print(f"======{cls.name}======")
        print("피자 준비 중")

    def bake(self):
        print("피자 굽는 중")

    def cut(self):
        print("피자 자르는 중")

    def box(self):
        print("피자 박스에 담기")


class CheesePizza(Pizza):
    name = "치즈 핏자"


class ClamPizza(Pizza):
    name = "해산물 핏자"
