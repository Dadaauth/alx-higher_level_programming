#!/usr/bin/python3
"""this is a module with only the Rectangle class
It is a module created for my project
"""

import Base from base


class Rectangle(Base):
    """A rectabgle class for this module
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init function documentation
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        a width property or attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width propertry setter
        """
        self.__width = value

    @property
    def height(self):
        """
        an height property or attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        an height property setter
        """
        self.__height = value

    @property
    def x(self):
        """
        an x property or attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        an x property setter
        """
        self.__x = value

    @property
    def y(self):
        """
        a y property or atribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        a y property setter 
        """
        self.__y = value
