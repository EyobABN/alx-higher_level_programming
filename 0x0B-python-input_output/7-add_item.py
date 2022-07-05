#!/usr/bin/python3
"""
    module for adding items in a list and saving them
    to a file
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    lst = []
    for av in sys.argv[1:]:
        lst.append(av)
    with open('add_item.json', 'w+', encoding="utf-8") as f:
        try:
            tot = json.load(f).append(lst)
        except Exception:
            tot = lst
        json.dump(tot, f)
