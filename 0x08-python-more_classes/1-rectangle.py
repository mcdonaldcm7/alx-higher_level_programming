#!/usr/bin/python3
"""
This module contains the definition for a simple and empty Rectangle class
The Rectange class contains two private instance attribute named width and
height.

There are safety checks setup to ensure the private instance attribute are
always a valid type i.e Both width and height are always integers with values
equal to or greater than 0 (>= 0)
"""


class Rectangle:
    """
    A simple empty class named Rectangle
    This class contains checks to ensure that the private attributes width and
    height can only be assgined with valid types and values.
    i.e Only integers >= 0

    Attributes:
        height (int): Height of the rectangle
        width (int): Width of the rectangle
    """

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        A simple getter for the private width attribute
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for the private instance variable width

        Parameter(s)
        ------------
        value (int): Value to assign to the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        A simple getter for the private height attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for the private instance variable height

        Parameter(s)
        ------------
        value (int): Value to assign to the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
