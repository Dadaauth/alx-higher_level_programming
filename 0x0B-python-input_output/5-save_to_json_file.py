#!/usr/bin/python3
"""
a module for manipulating json and files
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that save a python object to a file
    as string
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))


# save_to_json_file({'name': 'clement', 'age': 24}, 'fromJson.txt')
