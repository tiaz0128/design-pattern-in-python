from abc import ABC, abstractmethod


class AbstractPullObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class AbstractPullSubject(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.observers: list[AbstractPullObserver] = []

    @abstractmethod
    def register_observer(self, o: AbstractPullObserver):
        pass

    @abstractmethod
    def remove_observer(self, o: AbstractPullObserver):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


class WeatherData(AbstractPullSubject):
    def __init__(self, temperature, humidity, pressure) -> None:
        super().__init__()
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def register_observer(self, o: AbstractPullObserver):
        self.observers.append(o)

    def remove_observer(self, o: AbstractPullObserver):
        self.observers.remove(o)

    def notify_observer(self):
        for observer in self.observers:
            observer.update()

    def measurements_changed(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.notify_observer()


class CurrentConditionsDisplay(AbstractPullObserver):
    def __init__(self, weather_data: WeatherData) -> None:
        super().__init__()

        self.weather_data = weather_data
        self.temperature = 0
        self.humidity = 0

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity

        self.display()

    def display(self):
        print(f"CurrentConditionsDisplay : {self.temperature}, {self.humidity}")


class StatisticsDisplay(AbstractPullObserver):
    def __init__(self, weather_data: WeatherData) -> None:
        super().__init__()
        self.weather_data = weather_data
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def update(self) -> None:
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.pressure = self.weather_data.pressure

        self.display()

    def display(self):
        print(
            f"StatisticsDisplay : {self.temperature}, {self.humidity}, {self.pressure}"
        )
