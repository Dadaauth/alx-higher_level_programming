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
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width <= 0 or self.__height <= 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        rep_str = ""
        a, b = 0, 0
        if self.__width == 0 or self.__height == 0:
            return ""
        while a < self.__height:
            while b < self.__width:
                rep_str += str(self.print_symbol)
                b += 1
            b = 0
            rep_str += '\n'
            a += 1
        rep_str = rep_str[:-1]
        return rep_str

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
