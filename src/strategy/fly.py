from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Fly")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("No Way")
