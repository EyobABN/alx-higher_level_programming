#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Except: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
