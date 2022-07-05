#!/usr/bin/python3
"""
    module for deserializing a JSON string
"""
import json


def from_json_string(my_str):
    """
        function for deserializing JSON string
    """
    return (json.loads(my_str))
