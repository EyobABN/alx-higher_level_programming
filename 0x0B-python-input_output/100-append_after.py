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

    for line in range(len(contents)):
        if search_string in contents[line]:
            if line < len(contents) - 1:
                contents.insert(line + 1, new_string)
            else:
                contents.append(new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        contents = "".join(contents)
        f.write(contents)
