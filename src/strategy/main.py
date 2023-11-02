from duck import (
    Duck,
    MallardDuck,
    RedheadDuck,
    RubberDuck,
    DecoyDuck,
)

from fly import FlyWithWings, FlyNoWay

if __name__ == "__main__":
    duck: Duck = MallardDuck(FlyWithWings())
    duck.display()
    duck.perform_fly()

    duck = RedheadDuck(FlyWithWings())
    duck.display()
    duck.perform_fly()

    duck = RubberDuck(FlyNoWay())
    duck.display()
    duck.perform_fly()

    duck = DecoyDuck(FlyNoWay())
    duck.display()
    duck.perform_fly()
