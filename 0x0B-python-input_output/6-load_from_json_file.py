#!/usr/bin/python3
"""
    module for loading JSON from file
"""
import json


def load_from_json_file(filename):
    """
        function for loading JSON from file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
