from pizza import Pizza
from simple_factory import SimplePizzaFactory


class PizzaStore:
    def __init__(self) -> None:
        self.factory = SimplePizzaFactory()

    def order_pizza(self, pizza_type) -> Pizza:
        pizza = self.factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
