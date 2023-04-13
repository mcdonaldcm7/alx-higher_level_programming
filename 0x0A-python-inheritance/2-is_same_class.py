#!/usr/bin/python3
"""
This module contains the definition for the is_same_class function which checks
if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class
    """

    return (type(obj) == a_class)
