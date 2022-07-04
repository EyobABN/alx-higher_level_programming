#!/usr/bin/python3
"""
    module for inheritance
"""


def inherits_from(obj, a_class):
    """
        function for inheritance
    """
    return issubclass(obj.__class__, a_class) and a_class is not bool
