from factory.abstract_factory.abstract_factory import (
    ChicagoPizzaFactory,
    NYPizzaFactory,
)

from factory.abstract_factory.pizza_store import PizzaStore


def test_method_factory():
    ny_factor = NYPizzaFactory()
    ny_store = PizzaStore(ny_factor)
    ny_store.order()

    ch_factory = ChicagoPizzaFactory()
    ch_store = PizzaStore(ch_factory)
    ch_store.order()
