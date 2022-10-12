#!/usr/bin/python3
"""Module for Square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Setter for size attribute"""
        return self.width

    @size.setter
    def size(self, size):
        """Getter for size attribute"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attributes of this polygon.

        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'size', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary representation of this polygon.

        Returns:
            dict: A dictionary representation of this polygon.
        """
        res = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return res
