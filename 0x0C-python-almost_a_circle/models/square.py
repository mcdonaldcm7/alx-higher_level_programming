#!/usr/bin/python3
"""
This module contains the Square class which is a part of the 'models' package.
It inherits the the Rectangle class and overrides some of it's inherited method
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class which serves as representation of a real world Square object
    with attributes and method to access, manipulate and define it's properties
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """
        Defining the string representation of the Square class
        """

        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        Getter for the size property
        """

        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setter for the size property with type checks
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the current instance
        """

        if args is not None and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                    self.height = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the current object instance
        """

        return ({
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            })
