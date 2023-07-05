#!/usr/bin/python3
"""
A square printing module
has oonly one functon to print squares
but has a lot of functionalities and error handling
hoping to add more functions to this module
at a later date
"""


def print_square(size):
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        size = int(size)
    for i in range(0, size):
        for b in range(0, size):
            print("#", end='')
        print()
