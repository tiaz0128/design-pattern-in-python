from collections import Counter

from beverage import Beverage, Espresso, HouseBlend, Mocha

if __name__ == "__main__":
    beverage_1: Beverage = Espresso()
    beverage_1 = Mocha(beverage_1)
    beverage_1 = Mocha(beverage_1)

    print(f"name: {Counter(beverage_1.get_description())} cost: ${beverage_1.cost()}")

    beverage_2: Beverage = HouseBlend()
