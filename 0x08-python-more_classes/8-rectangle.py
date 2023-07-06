#!/usr/bin/python3
"""A rectangle module
"""


class Rectangle:
    """The rectangle class  for this
    module.
    Contains a lot of functions including the
    ones needed to instantiate the object
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
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
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return perimeter
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rect += str(self.print_symbol)
            rect += "\n"
        rect = rect[:-1]
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 == area_2 or area_1 > area_2:
            return rect_1
        if area_1 < area_2:
            return rect_2
