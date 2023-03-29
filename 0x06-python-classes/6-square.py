#!/usr/bin/python3
"""
This module contains a fairly simple Square class with safety checks for the
private instance variable __size and an area method to compute and return the
area of the square based on the size given.

It also comprise of a getter and a setter to get and set the private instance
variable size. Type checks and value checks are also included to ensure only
integer values greater than 0 can be set.
    The my_print method prints a square with the '#' character, the size of the
square depends on the size attribute
"""


class Square:
    """Square class contains safety checks for the private instance variable
    __size. It must be an integer with value greater than or equal 0

    The __init__ function handles the initialization of the size variable

    Attributes:
        size (int): Size of the square
        position (tuple): Coordinate of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is int:
            self.__size = size
            self.__position = position
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

    def my_print(self):
        """
        Prints position[1] number of lines
        Prints '_' position[0] times
        Prints a square to the stdout using the character #
        Prints a new line if the size is 0
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] > 0 and (self.__position[1] - 1) == i:
                    print()
                print(' ' * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """
        A getter to safely retrieve the instance position attribute
        of the Square class.

        Returns:
            self.__position attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets the value of the private instance attribute position to the value
        argument passed, Saftey checks regarding the type of value, length of
        value, and the type of the contents of value will be carried out.

        Args:
            value (tuple): Value to set position to
        """
        if (type(value) is tuple and len(value) == 2
                and (type(value[0]) is int) and (type(value[1]) is int) and
                    (value[0] >= 0 and value[1] >= 0)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
