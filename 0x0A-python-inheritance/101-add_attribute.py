#!/usr/bin/python3
"""
    module for adding a new attribute
"""


def add_attribute(obj, name, value):
    """
        function that adds a new attribute to an object
    """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
