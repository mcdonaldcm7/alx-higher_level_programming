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
    Furthermore, Rectangle also defines implements it's own __str__ and
__repr__ function. The __str__ method uses the '#' character to print a
rectangle with a dimension corresponding to that of the Rectangle's instance.
The __repr__ returns a string representation of the rectangle to be able to
a new instance by using eval().
    A public class attribute named number_of_instances keeps track of the
number of Rectangle instances there are and another public class attribute
named print_symbol keeps the symbols to be used to draw the squares across
instances.
    An addition to the module is the bigger_or_equal static method which
can be use to compare two rectangles together.
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

    number_of_instances = 0
    print_symbol = '#'

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
        type(self).number_of_instances += 1

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
                rect += str(self.print_symbol)
            if (i + 1) != self.__height:
                rect += '\n'
        return (rect)

    def __repr__(self):
        """
        Returns a string representation of Rectangle that can be used to
        recreate a new instance by using 'eval()'
        """
        return ("Rectangle({0:d}, {1:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A static method that returns the biggest rectangle based on the area
        This method also raises an exception (TypeError) if the wrong type was
        supplied.

        Returns rect_1 if rect_1 >= rect_2, Otherwise it returns rect_2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This class method returns a new instance of the Rectangle class with
        width == height == size (In other words a square :)
        """
        try:
            if not isinstance(size, int):
                raise TypeError("width must be an integer")
            if size < 0:
                raise ValueError("width must be >= 0")
        finally:
            return (cls(size, size))
