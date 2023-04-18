#!/usr/bin/python3
"""
This module contains the 'Base' class which will serve as the base of other
classes
"""


import json


class Base:
    """
    This class will manage the id attribute in all future classes and to avoid
    duplicating the same code
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{0:s}.json".format(cls.__name__)

        with open(filename, 'w') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(json.dumps([]))
            else:
                dict_list = []
                for objs in list_objs:
                    dic = objs.to_dictionary()
                    dict_list.append(dic)
                json_string = Base.to_json_string(dict_list)
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(3, 5, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        pass
