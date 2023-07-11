#!/usr/bin/python3
"""
returns the dict that works the magic
"""
import json


def class_to_json(obj):
    """
    returns the dict that works the magic
    """
    return obj.__dict__
