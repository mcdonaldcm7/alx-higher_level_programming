#!/usr/bin/python3
"""
This module contains the 'Base' class which will serve as the base of other
classes
"""


import json
import os


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

        if (list_dictionaries is None):
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """

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
        """
        Returns the list of the JSON string representation json_string
        """

        if (json_string is None):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """

        dummy = None
        if "size" in dictionary.keys():
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a file. The filename is the
        '<cls.__name__>.json'
        """

        filename = "{0:s}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return ([])
        dict_list = None
        ret = []
        with open(filename, 'r') as f:
            dict_list = cls.from_json_string(f.read())
        for i in dict_list:
            ret.append(cls.create(**i))
        return (ret)
