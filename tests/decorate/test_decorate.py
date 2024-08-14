import pytest
from collections import Counter

from decorate.beverage import Beverage, Espresso, HouseBlend, Mocha, Soy


def test_decorate():
    beverage: Beverage = Espresso()

    a = Mocha(beverage)
    b = Mocha(a)
    c = Soy(b)

    print(f"name: {Counter(c.get_description())} cost: ${c.cost()}")
