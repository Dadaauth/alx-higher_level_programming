#!/usr/bin/python3
"""
a module for appending to files
"""


def append_write(filename="", text=""):
    """
    a function for appending to files
    """
    with open(filename, 'a') as f:
        return f.write(text)
