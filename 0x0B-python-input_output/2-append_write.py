#!/usr/bin/python3
"""
    module for appending string at the end of a text file
"""


def append_write(filename="", text=""):
    """
        function for appending string to a text file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
