#!/usr/bin/python3
"""
Module Documentation
Not Just words
    I love to work hard
"""
class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
    
