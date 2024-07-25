from factory.simple_factory.pizza_store import PizzaStore
from factory.simple_factory.simple_factory import PizzaType


def test_simple_factory():
    pizza_store = PizzaStore()

    pizza_store.order(PizzaType.CHEESE_PIZZA)
    pizza_store.order(PizzaType.CLAM_PIZZA)
