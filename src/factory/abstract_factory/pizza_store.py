from factory.abstract_factory.abstract_factory import AbstractFactory


class PizzaStore:
    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def order(self):
        cheese = self.factory.make_cheese()
        dough = self.factory.make_dough()

        return self.make_pizza(cheese, dough)

    def make_pizza(self, cheese, dough):
        print(f"{self.factory.name}에서 받은")
        print(f"{cheese} 치즈와 {dough} 도우를 사용하여 피자를 만듭니다.")
