#!/usr/bin/python3
"""
This module contains the definition for the lookup function which returns a
list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of the attributes and methods of obj
    """

    return (dir(obj))
