import push_observer as push
import pull_observer as pull


def push_observer():
    """push 방식 : Subject --> Observer : push"""
    weather_data = push.WeatherData(10, 20, 30)

    current_conditions_display = push.CurrentConditionsDisplay()
    statistics_display = push.StatisticsDisplay()

    weather_data.register_observer(current_conditions_display)
    weather_data.register_observer(statistics_display)
    weather_data.measurements_changed(20, 30, 40)


def pull_observer():
    """pull 방식 Observer --> Subject : pull"""
    weather_data = pull.WeatherData(10, 20, 30)

    current_conditions_display = pull.CurrentConditionsDisplay(weather_data)
    statistics_display = pull.StatisticsDisplay(weather_data)

    weather_data.register_observer(current_conditions_display)
    weather_data.register_observer(statistics_display)

    weather_data.measurements_changed(99, 50, 23)


if __name__ == "__main__":
    push_observer()
    pull_observer()
