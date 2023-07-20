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

    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_l = []
        for inst in list_objs:
            new_l.append(inst.to_dictionary())
        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(cls.to_json_string(new_l))
