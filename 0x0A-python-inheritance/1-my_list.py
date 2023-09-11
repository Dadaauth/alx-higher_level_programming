#!/usr/bin/python3
"""
creates a class called myList that
inherits from the list class
"""


class MyList(list):
    """
    MyList class an exact replica of the list
    class in python
    Difference -/
        It has a function {print_sorted} that
        prints a sorted version of the list
    """
    def print_sorted(self):
        print(sorted(self))
