#!/usr/bin/python3
"""
    module for MyInt
"""


class MyInt(int):
    """
        class for MyInt
    """
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        if self.__value == other.real:
            return False
        return True

    def __ne__(self, other):
        if self.__value == other.real:
            return True
        return False
