#!/usr/bin/python3
"""
This module contains the definition for append_write which appends a string at
the end of a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append text to file name and return the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
