#!/usr/bin/python3
"""
    module for append after
"""


def append_after(filename="", search_string="", new_string=""):
    """
        function for append after
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        contents = f.readlines()

    new_contents = []
    for line in range(len(contents)):
        new_contents += contents[line]
        if search_string in contents[line]:
            new_contents += new_string

    with open(filename, 'w', encoding="utf-8") as f:
        new_contents = "".join(new_contents)
        f.write(new_contents)
