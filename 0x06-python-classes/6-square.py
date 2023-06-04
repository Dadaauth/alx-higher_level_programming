#!/usr/bin/python3
"""
A module containing a Square class with a lot of capabilities
"""


class Square:
    """
    a square class to create objects or instances of squares
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if isinstance(position, tuple) and len(position) == 2:
            if any(not isinstance(x, int) or x < 0 for x in position):
                raise TypeError("position must be a tuple"
                                " of 2 positive integers")
            else:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            a, b = self.__position
            y = 0
            z = 0
            while z < b:
                print("\n", end='')
                z += 1
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    while y < a:
                        print(" ", end='')
                        y += 1
                    print("#", end='')
                y = 0
                print()
