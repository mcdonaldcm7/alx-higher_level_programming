#!/usr/bin/python3
"""
This module contains the definition for the function save_to_json_file which
writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write my_obj using a JSON representation, to filename
    """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
