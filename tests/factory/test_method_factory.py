from factory.factory_method.pizza import PizzaType
from factory.factory_method.pizza_store import ChicagoPizzaStore, NYPizzaStore


def test_method_factory():
    ny_store = NYPizzaStore()
    ny_store.order(PizzaType.CHEESE)

    print("\n")

    chicago_store = ChicagoPizzaStore()
    chicago_store.order(PizzaType.CHEESE)
