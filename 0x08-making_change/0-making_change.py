#!/usr/bin/env python3
"""Change making module.
"""


def makeChange(coins, total):

    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    counter = 0
    coin_index = 0
    sub_value = total
    n = len(coins)

    while sub_value > 0:
        if coin_index > n:
            return -1

        if sub_value - sorted_coins[coin_index] >= 0:
            sub_value -= sorted_coins[coin_index]
            counter += 1
        else:
            coin_index += 1
    return counter
