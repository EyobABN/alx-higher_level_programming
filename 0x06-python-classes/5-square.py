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

    @property
    def size(self):
        """ getter function """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ public instance method that returns the area of the square """
        return self.size ** 2

    def my_print(self):
        """ public instance method that prints the square using # """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
