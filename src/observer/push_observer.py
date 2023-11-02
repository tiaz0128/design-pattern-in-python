from abc import ABC, abstractmethod


class AbstractPushObserver(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure) -> None:
        pass


class AbstractPushSubject(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.observers: list[AbstractPushObserver] = []

    @abstractmethod
    def register_observer(self, o: AbstractPushObserver):
        pass

    @abstractmethod
    def remove_observer(self, o: AbstractPushObserver):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


class WeatherData(AbstractPushSubject):
    def __init__(self, temperature, humidity, pressure) -> None:
        super().__init__()
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def register_observer(self, o: AbstractPushObserver):
        self.observers.append(o)

    def remove_observer(self, o: AbstractPushObserver):
        self.observers.remove(o)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.notify_observer()


class CurrentConditionsDisplay(AbstractPushObserver):
    def __init__(self) -> None:
        self.temperature = 0
        self.humidity = 0

    def update(self, temperature, humidity, pressure) -> None:
        self.temperature = temperature
        self.humidity = humidity

        self.display()

    def display(self):
        print(f"CurrentConditionsDisplay : {self.temperature}, {self.humidity}")


class StatisticsDisplay(AbstractPushObserver):
    def __init__(self) -> None:
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def update(self, temperature, humidity, pressure) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.display()

    def display(self):
        print(
            f"StatisticsDisplay : {self.temperature}, {self.humidity}, {self.pressure}"
        )
