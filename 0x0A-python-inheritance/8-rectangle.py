#!/usr/bin/python3
"""
This module contains the definition of a simple Rectangle class that inherits
from the 'BaseGeometry' class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A simple Rectangle class that inherits from BaseGeometry using the
    integer_validator function to assert the parameters for the Rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
