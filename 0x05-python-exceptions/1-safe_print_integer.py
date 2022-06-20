#!/usr/bin/python3
def safe_print_integer(value):
    ret = False
    try:
        print("{:d}".format(value))
        ret = True
    except ValueError:
        pass
    return ret
