#!/usr/bin/python3
"""
    module for writing a string to a text file
"""


def write_file(filename="", text=""):
    """
        function for writing a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text + '\n')
