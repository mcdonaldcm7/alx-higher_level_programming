#!/usr/bin/python3
"""
This module contains the definition for the read_file function that reads a
text file and prints it to stdout
"""


def read_file(filename=""):
    """
    Read's data from a text file and prints it to stdout
    """

    read_data = ""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
