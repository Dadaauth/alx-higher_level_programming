#!/usr/bin/python3
"""
Another version of isinstanceof
"""


def is_same_class(obj, a_class):
    """
    checks if an object is exactly an instance of
    a specified class
    """
    return type(obj) == a_class
