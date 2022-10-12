#!/usr/bin/python3
"""Module for Square object"""
from models.rectangle import Rectangle


def Square(Rectangle):
    """Square class that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__super__.__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
