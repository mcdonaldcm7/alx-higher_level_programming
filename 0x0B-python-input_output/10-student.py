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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        attrs is the list of attributes to return, if attrs is None return all
        """

        if attrs is None or len(attrs) == 0:
            return ({
                        'age': self.age,
                        'last_name': self.last_name,
                        'first_name': self.first_name
                })
        else:
            dic = {}
            for i in range(-1, (len(attrs))):
                if attrs[i] == 'first_name':
                    dic[attrs[i]] = self.first_name
                elif attrs[i] == 'last_name':
                    dic[attrs[i]] = self.last_name
                elif attrs[i] == 'age':
                    dic[attrs[i]] = self.age
            return (dic)
