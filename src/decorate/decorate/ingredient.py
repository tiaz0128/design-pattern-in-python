from decorate.decorate.decorator import Decorator


class Milk(Decorator):
    def cost(self):
        return super().cost() + 500

    def recipe(self):
        return super().recipe() + ["Milk"]


class Mocha(Decorator):
    def cost(self):
        return super().cost() + 1000

    def recipe(self):
        return super().recipe() + ["Mocha"]
