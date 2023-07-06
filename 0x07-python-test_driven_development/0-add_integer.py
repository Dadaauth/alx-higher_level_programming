#!/usr/bin/python3
"""
A module for working with adding integers
This module works for addition of two integers
It also has error predictions and handling
"""


def add_integer(a, b=98):
    """
    add_integer function
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
