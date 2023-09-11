#!/usr/bin/python3
"""
module for reading a file and printing to stdout
"""


def read_file(filename=""):
    """
    a readfile function
    it also prints the content
    of the file to the stdout
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end='')
