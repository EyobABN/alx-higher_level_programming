#!/usr/bin/python3
""" Module for task 0 of 0x06-Python-classes project -
write an empty class Square that defines a square """


class Square:
    """ an empty class that defines a square """
    def __init__(self, size=0):
        """ initializer function for instantiated object(s) """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def size(self):
        """ getter function """
        return self.size

    def size(self, value):
        """ setter function """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        """ public instance method """
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        return self.size ** 2
