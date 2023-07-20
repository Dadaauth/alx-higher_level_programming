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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) == 0 or args is None:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'height', value)
                    setattr(self, 'width', value)
                else
                    setattr(self, key, value)
            return
        l_order = ['id', 'size', 'x', 'y']
        idx = 0
        for arg in args:
            if l_order[idx] == 'size':
                setattr(self, 'height', arg)
                setattr(self, 'width', arg)
            else
                setattr(self, l_order[idx], arg)
            idx += 1

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
