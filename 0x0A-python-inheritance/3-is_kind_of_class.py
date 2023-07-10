#!/usr/bin/python3
"""
checks if an object is a kind of a class
that means it goes deep. It even checks subclasses
"""

def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
