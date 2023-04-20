#!/usr/bin/python3
"""
This module contains the 'Base' class which will serve as the base of other
classes
"""


import json
import os
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects and stores them as csv files
        """

        filename = "{0:s}.csv".format(cls.__name__)
        data = []
        for objs in list_objs:
            row = [objs.id, objs.width, objs.height, objs.x, objs.y]
            data.append(row)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
        csvfile.close()

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the csv file with the format <class_name>.csv and returns
        a list of object instances initialized with the content of the file
        """

        filename = "{0:s}.csv".format(cls.__name__)
        data = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        csvfile.close()
        dict_list = []
        for row in data:
            row_dict = {}
            if row[1] == row[2]:
                row_dict["id"] = int(row[0])
                row_dict["size"] =  int(row[1])
                row_dict["x"] = int(row[3])
                row_dict["y"] = int(row[4])
            else:
                row_dict["id"] =  int(row[0])
                row_dict["width"] = int(row[1])
                row_dict["height"] =  int(row[2])
                row_dict["x"] = int(row[3])
                row_dict["y"] = int(row[4])
            dict_list.append(row_dict)
        ret = []
        for dictionary in dict_list:
            ret.append(cls.create(**dictionary))
        return (ret)
