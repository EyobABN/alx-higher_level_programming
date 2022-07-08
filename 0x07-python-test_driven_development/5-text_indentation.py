#!/usr/bin/python3
"""
    module for text_indentation
"""


def text_indentation(text):
    """
        function for text_indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            if i + 1 != len(text) and text[i + 1] in [' ', '\t']:
                i += 1
        i += 1
