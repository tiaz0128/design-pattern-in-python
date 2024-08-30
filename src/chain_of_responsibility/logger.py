from abc import ABC, abstractmethod
from enum import Enum, auto


class LogLevel(Enum):
    INFO = auto()
    DEBUG = auto()
    ERROR = auto()


class Logger(ABC):
    def __init__(self, level):
        self.level = level
        self.next = None

    def set_next(self, next_logger):
        self.next = next_logger

    def log(self, level, message):
        if level.value >= self.level.value:
            self.write(message)
        if self.next:
            self.next.log(level, message)

    @abstractmethod
    def write(self, message):
        pass


class ConsoleLogger(Logger):
    def write(self, message):
        print(f"Console: {message}")


class FileLogger(Logger):
    def write(self, message):
        print(f"File: {message}")


class EmailLogger(Logger):
    def write(self, message):
        print(f"Email: {message}")


def setup_chain():
    console = ConsoleLogger(LogLevel.INFO)
    file = FileLogger(LogLevel.DEBUG)
    email = EmailLogger(LogLevel.ERROR)

    console.set_next(file)
    file.set_next(email)

    return console
