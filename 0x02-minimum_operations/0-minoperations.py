#!/usr/bin/python3
"""A module for a function"""


def minOperations(n):
    """Function that accepts an argument and returns an integer or 0"""
    if n <= 1:
        return 0

    counter = 0
    finder = 2

    while n > 1:
        while n % finder == 0:
            counter += finder
            n //= finder
        finder += 1

    return finder
