#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    value_exists = False
    for key in a_dictionary:
        if a_dictionary[key] == value:
            value_exists = True
    if value_exists is False:
        return a_dictionary
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
