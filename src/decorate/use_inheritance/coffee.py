class Coffee:
    name = "coffee"

    def __init__(self):
        self._cost = 4000
        self._recipe = ["coffee"]

    def cost(self):
        return self._cost

    def recipe(self):
        return self._recipe


class LatteCoffee(Coffee):
    name = "milk coffee"

    def __init__(self):
        super().__init__()
        self._cost += 500
        self._recipe += ["Milk"]


class MochaCoffee(Coffee):
    name = "mocha coffee"

    def __init__(self):
        super().__init__()
        self._cost += 1000
        self._recipe += ["Mocha"]
