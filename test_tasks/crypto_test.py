import json
from time import time
from typing import NamedTuple

from requests import get

SCANNING_TIME = 3600
BASE_URL = 'https://api.binance.com'
PRICE_PATH = '/api/v3/ticker/price'


def time_dec(func):
    """A time decorator to measure the execution time of any function in the script"""
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполнения функции {func.__name__} равно {end - start} секунд.')
        return result

    return timer


class BinanceException(Exception):
    """Exception class"""
    def __init__(self, status_code, data):
        self.status_code = status_code
        if data:
            self.code = data['code']
            self.msg = data['msg']
        else:
            self.code = None
            self.msg = None
        message = f"{status_code} [{self.code}] {self.msg}"
        super().__init__(message)


class BinanceTimePrice(NamedTuple):
    """A class with NamedTuple link for get_time_price function"""
    responce_time: float
    price: float


# @time_dec
def get_time_price(url: str, params: dict[str, str]) -> BinanceTimePrice:
    """Function that is used to fill prices dict in main func with time:price items"""
    responce = get(url, params=params, timeout=10)
    if responce.status_code == 200:
        return BinanceTimePrice(time() * 1000,
                                float(json.loads(json.dumps(responce.json(), indent=2))['price']))
    raise BinanceException(status_code=responce.status_code, data=responce.json())


def main(currency1: str, currency2: str) -> None:
    """Main function for scanning prices on Binance market"""
    prices = {}
    currency1 = currency1.upper()
    currency2 = currency2.upper()
    params = {'symbol': f'{currency1}{currency2}'}
    url = f'{BASE_URL}{PRICE_PATH}'
    while True:
        time_price: BinanceTimePrice = get_time_price(url, params)
        prices_keys = prices.keys()
        prices[time_price.responce_time] = time_price.price
        if time_price.price <= max(prices.values()) * 0.99:
            print(f'{currency1}/{currency2} price dropped 1% compared to the max!')
        if max(prices_keys) - min(prices_keys) > SCANNING_TIME * 1000:
            prices.pop(min(prices_keys))
            # print('deleted oldest price')


if __name__ == '__main__':
    main('xrp', 'usdt')
