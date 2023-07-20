#!/usr/bin/python3
"""
A base module in a package
"""
import json


class Base:
    """
    A base class for the start of the project
    python almost a circle
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        the initialization function of the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the json representation of a list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a list of instance of the parent class Base to a file
        """
        new_l = []
        if list_objs is not None:
            for inst in list_objs:
                new_l.append(inst.to_dictionary())
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(cls.to_json_string(new_l))

    @staticmethod
    def from_json_string(json_string):
        """
        returns a list from a json string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
