#!/usr/bin/python3
"""
defines a class
The class has a method that allows us
to get the dictionary representation
of the class instance
"""


class Student:
    """
    A student class with a single method
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
