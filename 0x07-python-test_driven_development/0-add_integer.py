#!/usr/bin/python3
"""
A module for working with adding integers
This module works for addition of two integers
It also has error predictions and handling
it has only one function
hoping to add other functions though
"""


def add_integer(a, b=98):
    """
    add_integer function ::
    ::
        works by adding two integers together,
        has error handling funcionalities also
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
