#!/usr/bin/python3
"""
a module to write to files
"""


def write_file(filename="", text=""):
    """
    write to a file,
    overwrites existing contents
    """
    with open(filename, "w") as f:
        return f.write(text)
