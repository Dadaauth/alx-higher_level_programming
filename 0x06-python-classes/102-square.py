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
        if isinstance(size, int) or isinstance(size, float):
            # assert size < 0, "Optional Assertion message"
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be a number")

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

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()
