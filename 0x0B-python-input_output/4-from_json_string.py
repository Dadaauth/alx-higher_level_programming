#!/usr/bin/python3
"""
a module for manipulating json strings
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
