#!/usr/bin/python3
"""
returns the dict that works the magic
"""
import json


def class_to_json(obj):
    """
    returns a list of the attributes an object of a class
    """
    return obj.__dict__
