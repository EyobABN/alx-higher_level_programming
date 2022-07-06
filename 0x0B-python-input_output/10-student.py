#!/usr/bin/python3
"""
    module for Student to JSON
"""


class Student:
    """
        class for Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation of a Student instance
        """
        dct = {}
        if bool(attrs) and all(isinstance(elem, str) for elem in attrs):
            for elem in attrs:
                if hasattr(self, elem):
                    dct[elem] = self.__getattribute__(elem)
        else:
            dct = self.__dict__
        return dct
