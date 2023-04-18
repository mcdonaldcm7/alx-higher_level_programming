#!/usr/bin/python3
from models.base import Base


"""
This module contains the Ractangle class which is a subclass of the Base class,
It contains attributes that represents a Rectangle, type checks to ensure only
the right type is assigned, method to retrieve the properties of the Rectangle
class such as the height, width, x, y position, and the area
"""


class Rectangle(Base):
    """
    A class representation of a Rectangle with an x-y position, width and
    height, and an area. Also with checks for type safety
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for width
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for width with type checks
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for height with type safety
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """

        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter for x with type safety
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """

        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter for y with type safety
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the Rectangle instance
        """

        return (self.__width * self.__height)

    def display(self):
        """
        Displays the rectangle represented by Rectangle using the # character
        """

        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Defining a string representation for the Rectangle class
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Update the values of the current instance using the value from args or
        optionally kwargs
        """

        if args is not None and len(args) > 0:
            index = 0
            for i in args:
                if index == 0:
                    self.id = args[0]
                elif index == 1:
                    self.__width = args[1]
                elif index == 2:
                    self.__height = args[2]
                elif index == 3:
                    self.__x = args[3]
                elif index == 4:
                    self.__y = args[4]
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "y":
                    self.__y = value
                elif key == "x":
                    self.__x = value

    def to_dictionary(self):
        """
        Return a dictionary representation of the current instance
        """

        return ({
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
            })
