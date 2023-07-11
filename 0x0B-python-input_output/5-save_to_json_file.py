#!/usr/bin/python3
"""
a module for manipulating json and files
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))


# save_to_json_file({'name': 'clement', 'age': 24}, 'fromJson.txt')
