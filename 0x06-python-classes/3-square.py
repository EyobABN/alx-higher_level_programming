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
        self.__size = size

    def area(self):
        """ public instance method """
        return self.__size ** 2
