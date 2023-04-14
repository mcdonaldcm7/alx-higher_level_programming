#!/usr/bin/python3
"""
This module contains the definition for the write_file function which writes
a string to a text file and returns the number of character written
"""


def write_file(filename="", text=""):
    """
    Write text to filename and returns the number of character written
    """

    num = 0
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return (num)
