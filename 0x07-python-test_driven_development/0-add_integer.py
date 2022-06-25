#!/usr/bin/python3
"""
    Module for adding two integers
"""

def add_integer(a, b=98):
    """
        adds two integers
    """
    ca = type(a) is int or type(a) is float
    cb = type(b) is int or type(b) is float

    if not ca:
        raise TypeError("a must be an integer")
    if not cb:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
