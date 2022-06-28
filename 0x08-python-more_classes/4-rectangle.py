#!/usr/bin/python3
"""
    empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
        creates a Rectangle object
    """
    def __init__(self, width=0, height=0):
        """initializes a Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """builds the rectangle with the # symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (self.__height * (self.__width * "#" + "\n"))[:-1]

    def __repr__(self):
        """repr implementation"""
        return "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
