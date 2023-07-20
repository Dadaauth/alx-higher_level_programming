#!/usr/bin/python3
"""
A square module
Contains a class that inherits
from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square is a Rectangle with the same width and height
        This is a square class that inherits from
            a rectangle class
        This makes it easier to define our square class
            since it has a lot to inherit from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__height}"
