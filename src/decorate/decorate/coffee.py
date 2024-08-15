from typing import override
from decorate.decorate.beverage import Beverage


class Coffee(Beverage):
    name = "Coffee"

    @override
    def cost(self) -> int:
        return 5000

    @override
    def recipe(self) -> list[str]:
        return ["Coffee"]
