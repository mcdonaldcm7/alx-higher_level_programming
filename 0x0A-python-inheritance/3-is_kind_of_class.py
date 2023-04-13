#!/usr/bin/python3
"""
This module contains the definition for the is_kind_of_class function which
checks if an object is an instance of, or if the object is an instance of a
class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a subclass
    """

    return (type(obj) == a_class or isinstance(obj, a_class))
