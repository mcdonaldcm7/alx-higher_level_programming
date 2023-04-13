#!/usr/bin/python3
"""
This module contains the definition of the inherits_from function which checks
if an object is an instance of a class that inherits the specified class
(directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from a_class
    (directly or indirectly)
    """

    obj_typ = type(obj)
    return (issubclass(obj_typ, a_class) and obj_typ != a_class)
