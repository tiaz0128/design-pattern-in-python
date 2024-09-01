from typing import Self


class CoinHandler:
    def __init__(self, coin_value):
        self.coin_value = coin_value
        self.next = None

    def set_next(self, small_coin: Self) -> Self:
        self.next = small_coin
        return small_coin

    def handle(self, amount):
        if amount >= self.coin_value:
            num_coins = amount // self.coin_value
            remaining = amount % self.coin_value

            print(f"{self.coin_value}원 동전 {num_coins}개 사용")

            if remaining > 0 and self.next:
                self.next.handle(remaining)
        elif self.next:
            self.next.handle(amount)


class Coin500(CoinHandler):
    def __init__(self):
        super().__init__(500)


class Coin100(CoinHandler):
    def __init__(self):
        super().__init__(100)


class Coin50(CoinHandler):
    def __init__(self):
        super().__init__(50)


class Coin10(CoinHandler):
    def __init__(self):
        super().__init__(10)


def calculate_change(amount):
    coin_500 = Coin500()
    coin_100 = Coin100()
    coin_50 = Coin50()
    coin_10 = Coin10()

    coin_500.set_next(coin_100).set_next(coin_50).set_next(coin_10)

    print(f"{amount}원에 대한 거스름돈:")
    coin_500.handle(amount)
