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
        """
        Initializes the Square class with the Rectangle class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        The size property or attribute for the Square class
        """
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
        """
        update method to update the attributes of the Square instance
        It overides the update method from the parent class [Rectangle]
        """
        if len(args) == 0 or args is None:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'height', value)
                    setattr(self, 'width', value)
                else:
                    setattr(self, key, value)
            return

        l_order = ['id', 'size', 'x', 'y']
        idx = 0
        for arg in args:
            if l_order[idx] == 'size':
                setattr(self, 'height', arg)
                setattr(self, 'width', arg)
            else:
                setattr(self, l_order[idx], arg)
            idx += 1

    def to_dictionary(self):
        return {
                'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y
            }

    def __str__(self):
        """
        changes the string representation of the Square class
        Overides this method from the parent class [Rectangle]
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
