#!/usr/bin/python3
"""
    module for returning a JSON of a string
"""
import json


def to_json_string(my_obj):
    """
        function for serializing object
    """
    return (json.dumps(my_obj))
