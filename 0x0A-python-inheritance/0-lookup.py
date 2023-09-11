#!/usr/bin/python3
"""
A module to lookup the names defined
in an object
"""


def lookup(obj):
    """
    the lookup function
    used to lookup the names in
    the namespace of a particular object
    """
    return dir(obj)
