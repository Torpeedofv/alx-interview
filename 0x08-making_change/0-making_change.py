#!/usr/bin/python3
"""A module for a fucntion"""


def makeChange(coins, total):
    """function that determines the fewest number of coins needed
    to meet a given amount total"""
    if (total <= 0):
        return 0

    current_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        remnant = (total - current_total) // coin
        current_total += remnant * coin
        used_coins += remnant
        if current_total == total:
            return used_coins
    return -1
