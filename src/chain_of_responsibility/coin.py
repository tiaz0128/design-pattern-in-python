from abc import ABC, abstractmethod


class CoinHandler(ABC):
    def __init__(self, coin_value):
        self.coin_value = coin_value
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, amount):
        if amount >= self.coin_value:
            num_coins = amount // self.coin_value
            remaining = amount % self.coin_value

            print(f"{self.coin_value}원 동전 {num_coins}개 사용")

            if remaining > 0 and self.next_handler:
                self.next_handler.handle(remaining)
        elif self.next_handler:
            self.next_handler.handle(amount)


class Coin500Handler(CoinHandler):
    def __init__(self):
        super().__init__(500)


class Coin100Handler(CoinHandler):
    def __init__(self):
        super().__init__(100)


class Coin50Handler(CoinHandler):
    def __init__(self):
        super().__init__(50)


class Coin10Handler(CoinHandler):
    def __init__(self):
        super().__init__(10)


def calculate_change(amount):
    handler500 = Coin500Handler()
    handler100 = Coin100Handler()
    handler50 = Coin50Handler()
    handler10 = Coin10Handler()

    handler500.set_next(handler100).set_next(handler50).set_next(handler10)

    print(f"{amount}원에 대한 거스름돈:")
    handler500.handle(amount)
