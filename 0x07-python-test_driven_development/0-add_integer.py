#!/usr/bin/python3
"""
    Module for adding two integers
"""


def add_integer(a, b=98):
    """
        adds two integers
    """
    ca = type(a) is not int and type(a) is not float
    cb = type(b) is not int and type(b) is not float

    if a is None or ca:
        raise TypeError("a must be an integer")
    if cb:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
