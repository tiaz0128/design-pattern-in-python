from fly import FlyBehavior


class Duck:
    def __init__(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def display(self):
        print("Looks like Duck")

    def perform_fly(self):
        self.fly_behavior.fly()

    def set_fly_behavior(self, behavior: FlyBehavior):
        self.fly_behavior = behavior


class MallardDuck(Duck):
    def display(self):
        print("Mallard Duck")


class RedheadDuck(Duck):
    def display(self):
        print("Redhead Duck")


class RubberDuck(Duck):
    def display(self):
        print("Rubber Duck")


class DecoyDuck(Duck):
    def display(self):
        print("Decoy Duck")
