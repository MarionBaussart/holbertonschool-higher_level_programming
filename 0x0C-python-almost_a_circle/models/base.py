#!/usr/bin/python3
"""
module containing class Base
"""
import json


class Base:
    """ Base class
    private class attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base of a class
        Args:
            self: first argument to instance methods
            id: public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Serialize obj to a JSON formatted str
        Args:
            list_dictionaries: list of dictionaries
        Return: JSON string representation of list_dictionaries
        """
        json_dict = "[]"
        if list_dictionaries is not None and list_dictionaries is not []:
            json_dict = json.dumps(list_dictionaries)
        return json_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        Args:
            cls: first argument to class methods
            list_objs: list of instances who inherits of Base
        """
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        list_json = cls.to_json_string(list_dict)
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w") as file:
            file.write(list_json)

    @staticmethod
    def from_json_string(json_string):
        """ Deserialize a JSON string to a python list obj
        Args:
            json_string: string representing a list of dictionaries
        Return: the list obj represented by json_string
        """
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

