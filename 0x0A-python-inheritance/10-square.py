#!/usr/bin/python3
"""
This module contains the definition of a simple Rectangle class that inherits
the 'BaseGeometry' class
"""


class BaseGeometry:
    """
    This clas is the base class to be used for geometry with function that
    ensure the correct types and values are passed
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or not type(value) == int:
            raise TypeError("{0:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{0:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A simple Rectangle class that inherits the BaseGeometry using the
    integer_validator function to assert the parameters for the Rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def area(self):
        """
        Returns the are of the rectangle
        """

        return (self._width * self._height)

    def __str__(self):
        """
        Defining the string representation for the rectangle
        """

        return ("[Rectangle] {0:d}/{1:d}".format(self._width, self._height))


class Square(Rectangle):
    """
    A simple Square class that inherits the Rectangle class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self._height = size
        self._width = size
