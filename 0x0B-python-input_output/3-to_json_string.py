#!/usr/bin/python3
"""
a module for turning objects to JSON strings
"""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
