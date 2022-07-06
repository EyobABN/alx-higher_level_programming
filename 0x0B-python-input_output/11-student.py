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
        if isinstance(attrs, list):
            dct = {}
            for elem in attrs:
                if hasattr(self, elem):
                    dct[elem] = self.__getattribute__(elem)
        else:
            dct = self.__dict__
        return dct

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student instance with json
        """
        self.__dict__ = json
