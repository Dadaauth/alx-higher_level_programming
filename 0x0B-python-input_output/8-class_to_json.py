#!/usr/bin/python3
"""
handles the logic for gettign the attributes
an object has in a class scope or namespace
"""


def class_to_json(obj):
    """
    returns a list of the attributes an object of a class
    possesses
    """
    return obj.__dict__
