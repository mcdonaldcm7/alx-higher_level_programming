#!/usr/bin/python3
"""
This module contains the definiton for the function say_my_name, Which prints
the first name and last name passsed to the function argument
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the string "My name is <first_name> <last_name>"

    Parameter(s)
    ------------
    first_name (str): String argument representing the first name to print
    last_name (str): String input representing the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {0:s} {1:s}".format(first_name, last_name))
