#!/usr/bin/python3
"""
creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    loads an object form a file containing json
    """
    with open(filename, 'r') as f:
        return json.loads(f.read())


# print(load_from_json_file("fromJson.txt"))
