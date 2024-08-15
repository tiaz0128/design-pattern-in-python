from decorate.use_inheritance.coffee import Coffee, LatteCoffee, MochaCoffee


def test_decorate():
    coffee = Coffee()
    milk_coffee = LatteCoffee()
    mocha_coffee = MochaCoffee()

    print(f"{coffee.name} / recipe: {coffee.recipe()} / cost: {coffee.cost()}")
    print(
        f"{milk_coffee.name} / recipe: {milk_coffee.recipe()} / cost: {milk_coffee.cost()}"
    )
    print(
        f"{mocha_coffee.name} / recipe: {mocha_coffee.recipe()} / cost: {mocha_coffee.cost()}"
    )
