from factory.factory_method.method_factory import NYPizzaFactory, ChicagoPizzaFactory
from factory.factory_method.pizza import PizzaType
from factory.factory_method.pizza_store import PizzaStore


def test_method_factory():
    ny_factor = NYPizzaFactory()
    ny_store = PizzaStore(ny_factor)
    ny_store.order(PizzaType.CHEESE)

    print("\n")

    ch_factory = ChicagoPizzaFactory()
    ch_store = PizzaStore(ch_factory)
    ch_store.order(PizzaType.CHEESE)
