#!/usr/bin/python3
"""
This module contains a class called BaseGeometry
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
