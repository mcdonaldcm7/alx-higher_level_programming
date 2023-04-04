#!/usr/bin/python3
"""
This module defines a simple class that only allows the user to create a new
instance attribute, if it is called 'first_name'
"""


class LockedClass:
    __slots__ = ("first_name",)
