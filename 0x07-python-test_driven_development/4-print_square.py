#!/usr/bin/python3
"""
This module contains the function definition for print square.
print_square uses the ASCII character '#' to print a square, the size of
which is taken as argument from the function
"""


def print_square(size):
    """
    Prints a square using the '#' ASCII character.
    The square has size width and size height

    Parameter(s)
    ------------
    size (int): Size of the square to draw

    Example:
        >>> print_square(2)
        ##
        ##
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        for j in range(int(size)):
            print('#', end="")
        print()
