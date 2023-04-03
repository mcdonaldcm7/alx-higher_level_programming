#!/usr/bin/python3
"""
This module contains the definition for a simple and empty Rectangle class
The Rectange class contains two private instance attribute named width and
height.

There are safety checks setup to ensure the private instance attribute are
always a valid type i.e Both width and height are always integers with values
equal to or greater than 0 (>= 0)
    Additionally, Rectangle also contains two methods asides the init, getter,
and setter. Namely area and perimeter which can be used to retrieve the area
and the perimeter of the rectangle represented by the Rectangle class.
    Furthermore, Rectangle also defines implements it's own __str__ function
which uses the '#' character to print a rectangle with a dimension
corresponding to that of the Rectangle's instance
"""


class Rectangle:
    """
    A simple empty class named Rectangle
    This class contains checks to ensure that the private attributes width and
    height can only be assgined with valid types and values.
    i.e Only integers >= 0

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
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

    def area(self):
        """
        Computes and returns the area of the rectangle represented by the
        Rectangle class.

        Returns:
            Area of the Rectangle i.e width * height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle represented by the
        Rectangle class.

        Returns:
            Perimeter of the Rectangle i.e 2 * (width + height)
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Prints a rectangle with the current instance's dimension
        Rectangle will be printed with the '#' ASCII character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if (i + 1) != self.__height:
                rect += '\n'
        return (rect)
