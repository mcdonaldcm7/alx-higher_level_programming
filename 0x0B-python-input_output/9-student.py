#!/usr/bin/python3
"""
This module contains the definition for the Student class.
The student class defines its constructor and a 'to_json' function that
retrieves a dictionary represetation of a Student instance
"""


class Student:
    """
    A simple class representing a 'Student' with puclic instance attributes:
        - first_name
        - last_name
        - age

    This class also contains a method by name 'to_json' which returns a
    dictionary representation of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return ({
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
            })
