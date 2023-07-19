#!/usr/bin/python3
"""
A base module in a package
"""


class Base:
    """
    A base class for the start of the project
    python almost a circle
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
