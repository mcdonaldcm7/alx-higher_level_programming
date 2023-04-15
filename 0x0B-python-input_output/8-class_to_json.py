#!/usr/bin/python3
"""
This module contains the definition for the class_to_json function that returns
the dictionary description with simple data structure (list, dictionary, string
, integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Return dictionary description of obj
    """

    dic = vars(obj)
    return (dic)
