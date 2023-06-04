#!/usr/bin/python3
"""
Module Documentation
Not Just words
    I love to work hard
"""


class Square:
    """
    We are talking about the Square class
        Methods:
            __init__: initializes the instances created
            area: returns the area of the square
    """
    def __init__(self, size=0):
        """
        __init__ method: to initialize
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        returns the area of the square object
        """
        return self.__size * self.__size
