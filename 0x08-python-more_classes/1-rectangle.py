#!/usr/bin/python3
"""
A module holding the rectangular class to create
instances or objects of rectangles
"""


class Rectangle:
    """
    a Rectangle class to create rectangles
        Examples:
            >>> r = __import__("1-rectangle").Rectangle

            >>> my_rect = r(2, 3)

            >>> print(my_rect.__dict__)

            >>> my_rect.width = 12

            >>> my_rect.height = 34

            >>> print(my_rect.__dict__)
    """
    def __init__(self, width: int = 0, height: int = 0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
