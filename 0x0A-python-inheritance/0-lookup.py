#!/usr/bin/python3
"""
    module for a returning the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """
        function for returning list of available
        attributes and methods of an object
    """
    return dir(obj)
