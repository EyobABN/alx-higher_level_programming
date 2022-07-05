#!/usr/bin/python3
"""
    module for saving to a file in JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
        function that saves to a file using JSON
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
