#!/usr/bin/python3
"""
Module containing function definition for add_attribute
"""


def add_attribute(obj, name, value):
    """
    Adds an attribute to a class
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    dic = vars(obj)
    dic[name] = value
