#!/usr/bin/python3
"""this is a module with only the Rectangle class
It is a module created for my project
"""

import Base from base


class Rectangle(Base):
    """A rectangle class for this module that
    inherits from the Base class
    atributes:
        @height
        @width
        @x
        @y
        @id

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init function documentation or the class and forgive
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        a width property or attribute, this is a doc
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width propertry setter, this is a dioc
        """
        self.__width = value

    @property
    def height(self):
        """
        an height property or attribute, this is a doc
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        an height property setter, this is a doc
        """
        self.__height = value

    @property
    def x(self):
        """
        an x property or attribute, this is a doc
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        an x property setter, this is a doc
        """
        self.__x = value

    @property
    def y(self):
        """
        a y property or atribute, this is a doc
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        a y property setter, this is a doc
        """
        self.__y = value
