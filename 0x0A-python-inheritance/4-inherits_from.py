#!/usr/bin/python3
"""
checks if an object's class is a subclass of a
specified class
"""


def inherits_from(obj, a_class):
    """
    compares an objects class and the specified class
    checks for subclases
    """
    return issubclass(type(obj), a_class)
