#!/usr/bin/python3
"""A module for a method that determines if
a given data set represents a valid utf-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    byte = 0
    for number in data:
        if number >> 6 == 0b10:
            if byte == 0:
                return False
            byte -= 1
        else:
            if byte > 0:
                return False
            if number >> 7 == 0b0:
                byte = 0
            elif number >> 5 == 0b110:
                byte = 1
            elif number >> 4 == 0b1110:
                byte = 2
            elif number >> 3 == 0b11110:
                byte = 3
            else:
                return False
    if byte > 0:
        return False

    return True
