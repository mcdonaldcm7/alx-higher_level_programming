#!/usr/bin/python3
"""
This module defines a simple class that only allows the user to create a new
instance attribute, if it is called 'first_name'
"""


class LockedClass:
    """
    This class only allows the creation of an instance variable named
    'first_name'
    """
    __slots__ = ("first_name",)
