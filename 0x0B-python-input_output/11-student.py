#!/usr/bin/python3
"""
defines a class
The class has a method that allows us
to get the dictionary representation
of the class instance
"""


class Student:
    """
    A student class with a two methods
    a simple way to learn about serialization
    and deserialization
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        if attrs is None:
            return self.__dict__
        t_dict = self.__dict__.copy()
        for key, value in self.__dict__.items():
            if key not in attrs:
                del t_dict[key]
        return t_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
