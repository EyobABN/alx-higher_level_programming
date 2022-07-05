#!/usr/bin/python3
"""
    module for reading a text file and printing to stdout
"""


def read_file(filename=""):
    """
        a function that reads a text file and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
