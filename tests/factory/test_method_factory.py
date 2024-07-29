from factory.factory_method.method_factory import NYPizzaFactory, ChicagoPizzaFactory
from factory.factory_method.pizza import PizzaType
from factory.factory_method.pizza_store import PizzaStore


def test_method_factory():
    ny_store = NYPizzaFactory()
    ny_pizza_store = PizzaStore(ny_store)
    ny_pizza_store.order(PizzaType.CHEESE)

    print("\n")

    ch_factory = ChicagoPizzaFactory()
    chicago_store = PizzaStore(ch_factory)
    chicago_store.order(PizzaType.CHEESE)
