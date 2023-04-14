#!/usr/bin/python3
"""
This module contains the function definition for 'load_from_json_file' which
creates an object from a 'JSON file'
"""


import json


def load_from_json_file(filename):
    """
    Return object created from the JSON file 'filename'
    """

    obj = ""
    with open(filename, 'r') as f:
        obj = f.read()
    return (json.loads(obj))
