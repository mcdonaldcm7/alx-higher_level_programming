#!/usr/bin/python3
"""
This module contains a simple MyInt class that inherits the int class
and overloads two of it's operators
"""


class MyInt(int):
    """
    SImple class to override the overloaded operators '==' and '!='
    """

    def __eq__(self, other):
        """
        Overriding int's equal to operator
        """

        return (int.__ne__(self, other))

    def __ne__(self, other):
        """
        Overriding int's not equal to operator
        """

        return (int.__eq__(self, other))
