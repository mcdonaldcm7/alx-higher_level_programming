#!/usr/bin/python3
"""
Module containing function definition for add_attribute
"""


def add_attribute(obj, name, value):
    """
    Adds an attribute to a class
    """

    dic = vars(obj)
    dic[name] = value
