#!/usr/bin/python3
"""
this is a module with only the Rectangle class
It is a module created for my project
"""
from models.base import Base


class Rectangle(Base):
    """
    The rectangle class, inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init function documentation or the class and forgive
        this is the function that inititalizes the Rectangle class
        """
        v_int = "{} must be an integer"
        v_size = "{} must be > 0"
        v_size_xy = "{} must be >= 0"
        if not isinstance(width, int):
            raise TypeError(v_int.format("width"))
        if not isinstance(height, int):
            raise TypeError(v_int.format("height"))
        if not isinstance(x, int):
            raise TypeError(v_int.format("x"))
        if not isinstance(y, int):
            raise TypeError(v_int.format("y"))
        if width <= 0:
            raise ValueError(v_size.format("width"))
        if height <= 0:
            raise ValueError(v_size.format("height"))
        if x < 0:
            raise ValueError(v_size_xy.format("x"))
        if y < 0:
            raise ValueError(v_size_xy.format("y"))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """
        a call to the super class of the Rectangle class
        """
        super().__init__(id)

    @property
    def width(self):
        """
        a width property or attribute, this is a doc
        this is a prioperty for the doc
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        an height property or attribute, this is a doc
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        an x property or attribute, this is a doc
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        a y property or atribute, this is a doc
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates and returns the area of the rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """
        displays the rectangle instance in terms of the width and height
        using a particular symbol to represent each space
        i.e:
            Rectangle(2, 4) will give =>

                ##
                ##
                ##
                ##
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end='')
            for _ in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """
        a __str__ method to change how the Rectangle class instances
        are represented...
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"\
               f" - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        updates the rectangle instance attributes from a tuple of
        arguments or *args
        """
        if len(args) == 0 or args is None:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        l_order = ["id", "width", "height", "x", "y"]
        idx = 0
        for arg in args:
            setattr(self, l_order[idx], arg)
            idx += 1

    def to_dictionary(self):
        """
        returns the dictionary representation of the Rectangle instance
        """
        return {
                'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y
            }
