#!/usr/bin/python3
"""
This module contains the MyList class which inherits the list class and adds
a new method called print_sorted 
"""


class MyList(list):
    """
    Inherits the list class and add the print_sorted function which prints
    the list but sorted
    """

    def print_sorted(self):
        cpy = self.copy()
        cpy.sort()
        print(cpy)
