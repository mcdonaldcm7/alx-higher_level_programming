#!/usr/bin/python3
"""
This module contains a fairly simple Square class with safety checks for the
private instance variable __size
"""


class Square:
    """Square class contains safety checks for the private instance variable
    __size. It must be an integer with value greater than or equal 0

    The __init__ function handles the initialization of the size variable

    Attributes:
        size (int): Size of the square
    """
    def __init__(self, size=0):
        if type(size) is int:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculate and returns the area of the square based on the size given

        Returns:
            Area of the square
        """
        return (self.__size ** 2)
