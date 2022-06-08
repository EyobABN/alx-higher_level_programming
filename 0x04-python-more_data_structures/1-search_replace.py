#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [old if old != search else replace for old in my_list]
    return new_list
