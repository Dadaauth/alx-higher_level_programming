#!/usr/bin/python3
"""
A base module in a package
"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance
        """
        dummy = cls(10, 10)
#        print("dictionarty: ", dictionary)
#        print("dummy: ", dummy)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loads an instance from a file
        """
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                instance_list = []
                instance_list_dict = cls.from_json_string(f.read())
                for i_list in instance_list_dict:
                    instance_list.append(cls.create(**i_list))
                return instance_list
        except FileNotFoundError:
            # the file doesn't exist
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in csv
        """
        new_l = []
        if list_objs is not None:
            for inst in list_objs:
                new_l.append(inst.to_dictionary())
        with open(f"{cls.__name__}.csv", 'w') as f:
            for inst in new_l:
                f_str = ""
                for key, value in inst.items():
                    f_str += f"{value},"
                f_str = f_str[:-1]
                f.write(f_str + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes a csv file
        """
        try:
            with open(f"{cls.__name__}.csv", 'r') as csvfile:
                instance_list = []
                instance_list_dict = csv.reader(csvfile)
                for row in instance_list_dict:
                    if cls.__name__ == 'Rectangle':
                        dictionary = {
                                'id': int(row[0]), 'width': int(row[1]),
                                'height': int(row[2]), 'x': int(row[3]),
                                'y': int(row[4])
                            }
                    if cls.__name__ == 'Square':
                        dictionary = {
                                'id': int(row[0]), 'size': int(row[1]),
                                'x': int(row[2]), 'y': int(row[3])
                                }
                    instance_list.append(cls.create(**dictionary))
                return instance_list
        except FileNotFoundError:
            # the file doesn't exist
            return []
