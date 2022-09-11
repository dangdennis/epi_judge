from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_profit, min_stock_price = 0, prices[0]
    max_profits_per_day = [0] * len(prices)
    # first pass captures the best profits we can make in one trade
    for i, price in enumerate(prices):
        max_profit = max(max_profit, price - min_stock_price)
        min_stock_price = min(price, min_stock_price)
        max_profits_per_day[i] = max_profit
        
    # working backwards, we capture potential profit for a second trade
    # as we iterate backwards, we capture and sum the second trade's profit with the previous trade's profit
    # because these trades are legal and gauranteed that it's made after the first trade's day
    max_stock_price = prices[-1]
    for i, price in reversed(list(enumerate(prices))):
        max_stock_price = max(max_stock_price, price)
        max_profit = max(max_profit, max_stock_price - price + max_profits_per_day[i])
        
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
