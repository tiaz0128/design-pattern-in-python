from decorate.decorate.beverage import Beverage


class Decorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def cost(self) -> int:
        return self.beverage.cost()

    def recipe(self) -> list[str]:
        return self.beverage.recipe()
