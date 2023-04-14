#!/usr/bin/python3
"""
This module contains the definition for the function from_json_string which
returns an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Return decoded JSON object
    """

    return (json.loads(my_str))
