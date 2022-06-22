#!/usr/bin/python3
""" Module for task 0 of 0x06-Python-classes project -
write an empty class Square that defines a square """


class Square:
    """ an empty class that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ initializer function for instantiated object(s) """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple)) or \
                (len(position) != 2) or \
                (not isinstance(position[0], int)) or \
                (not isinstance(position[1], int)) or \
                (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ getter function """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter function """
        if (not isinstance(value, tuple)) or \
                (len(value) != 2) or \
                (not isinstance(value[0], int)) or \
                (not isinstance(value[1], int)) or \
                (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ public instance method that returns the area of the square """
        return self.size ** 2

    def my_print(self):
        """ public instance method that prints the square using # """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
