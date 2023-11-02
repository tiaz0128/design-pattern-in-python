from pizza import PizzaType
from pizza_store import NYPizzaStore, ChicagoPizzaStore


if __name__ == "__main__":
    ny_store = NYPizzaStore()
    ny_store.order_pizza(PizzaType.CHEESE)

    print("\n")

    chicago_store = ChicagoPizzaStore()
    chicago_store.order_pizza(PizzaType.CHEESE)
