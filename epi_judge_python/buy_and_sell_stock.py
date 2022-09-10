import math
from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    maximum_profit = 0
    min_price_so_far = float('inf')
    for price in prices:
        todays_profit = price - min_price_so_far
        maximum_profit = max(maximum_profit, todays_profit)
        min_price_so_far = min(min_price_so_far, price)
    return maximum_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
