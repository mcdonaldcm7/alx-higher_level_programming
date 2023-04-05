#!/usr/bin/python3
"""
This module contains an add_integer method which basically computes and returns the addition of both integer parameters
"""


def add_integer(a, b=98):
    """
    This function takes in two integer argument and returns the sum

    Example:
        >>> add_integer(3, 7)
        10

    Parameters
    ----------
        a (int): First digit
        b (int): Second digit, default = 98

    Return (a + b)
    """
    result = 0
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return (result)
