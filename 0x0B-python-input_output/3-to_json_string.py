#!/usr/bin/python3
"""
This module contains the definition for the function to_json_string which
returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Return json representation of my_obj
    """

    return (json.dumps(my_obj))
