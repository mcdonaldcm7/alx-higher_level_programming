#!/usr/bin/python3
"""
This module contains a fairly simple Square class with safety checks for the
private instance variable __size and an area method to compute and return the
area of the square based on the size given.

The square class also includes a getter and a setter for the private variable
size
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

    @property
    def size(self):
        """
        A safe way to read the __size attribute from the Square class

        Returns:
            __size variable
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the value of the private instance variable size to the argument
        passed. value has to be an integer with value greater than 0, else
        a TypeError or a ValueError will be raised

        Args:
            value (int): Value to set size to
        """
        if type(value) is int:
            self.__size = value
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        """
        Overloading the equal to (==) operator so it compares the sizes of both
        squares and returns a boolean value based on the result of the
        comparison

        e.g sq1 = Square(4)
            sq2 = Square(4)

            if sq1 == sq2:
                print("sq1 equals sq2")
            else:
                print("sq1 not equals sq2")
        """
        return (True if self.__size == other.size else False)

    def __ne__(self, other):
        """
        Overloading the not equal to (!=) operator so it compares the sizes of
        both squares and returns a boolean value based on the result of the
        comparison

        e.g sq1 = Square(4)
            sq2 = Square(5)

            if sq1 != sq2:
                print("sq1 does not equal sq2")
            else:
                print("sq1 equals to sq2")
        """
        return (True if self.__size != other.size else False)

    def __gt__(self, other):
        """
        Overloading the greater than to (>) operator so it compares the sizes
        of both squares and returns a boolean value based on the result of the
        comparison

        e.g sq1 = Square(10)
            sq2 = Square(7)

            if sq1 > sq2:
                print("sq1 is greater than sq2")
            else:
                print("sq1 is not greater than sq2")
        """
        return (True if self.__size > other.size else False)

    def __ge__(self, other):
        """
        Overloading the greater than or equal to (>=) operator so it compares
        the sizes of both squares and returns a boolean value based on the
        result of the comparison

        e.g sq1 = Square(7)
            sq2 = Square(7)

            if sq1 >= sq2:
                print("sq1 is greater than or equal to sq2")
            else:
                print("sq1 is not greater than or equal to sq2")
        """
        return (True if self.__size >= other.size else False)

    def __lt__(self, other):
        """
        Overloading the less than (<) operator so it compares the sizes of
        both squares and returns a boolean value based on the result of the
        comparison

        e.g sq1 = Square(3)
            sq2 = Square(7)

            if sq1 < sq2:
                print("sq1 is less than sq2")
            else:
                print("sq1 is not less than sq2")
        """
        return (True if self.__size < other.size else False)

    def __le__(self, other):
        """
        Overloading the less than or equal to (<=) operator so it compares the
        sizes of both squares and returns a boolean value based on the result
        of the comparison

        e.g sq1 = Square(10)
            sq2 = Square(10)

            if sq1 <= sq2:
                print("sq1 is less than or equal to sq2")
            else:
                print("sq1 is not less than or equal to sq2")
        """
        return (True if self.__size <= other.size else False)
