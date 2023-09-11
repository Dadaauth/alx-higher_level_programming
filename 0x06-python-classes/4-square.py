#!/usr/bin/python3
"""
This module initializes a private object variable
with an opttional size
"""


class Square:
    """
    the Square class, more information coming soon.
    """
    def __init__(self, size=0):
        """
        the init method
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
