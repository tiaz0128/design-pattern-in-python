from decorate.decorate.beverage import Beverage
from decorate.decorate.coffee import Coffee
from decorate.decorate.ingredient import Mocha, Milk


def test_decorate():
    beverage: Beverage = Coffee()

    a = Mocha(beverage)
    b = Mocha(a)
    c = Milk(b)

    print(f"{c.recipe()} / cost: {c.cost()}")
