#!/usr/bin/python3
"""
a module for manipulating json strings
"""
import json


def from_json_string(my_str):
    """
    a function to change a json string to a
    python object
    """
    return json.loads(my_str)
