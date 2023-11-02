from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.description = ""

    def get_description(self):
        return [self.description]

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "에스프레소"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "하우스블랜드"

    def cost(self):
        return 1.24


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__()
        self.beverage = beverage

    @abstractmethod
    def get_description(self):
        pass


class Mocha(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ["Mocha"]

    def cost(self):
        return self.beverage.cost() + 0.2


class Soy(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ["Soy"]

    def cost(self):
        return self.beverage.cost() + 0.2
