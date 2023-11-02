from pizza_store import PizzaStore
from simple_factory import PizzaType
import sys

if __name__ == "__main__":
    print(sys.version_info)

    pizza_store = PizzaStore()

    pizza_store.order_pizza(PizzaType.CHEESE_PIZZA)
    pizza_store.order_pizza(PizzaType.CLAM_PIZZA)
