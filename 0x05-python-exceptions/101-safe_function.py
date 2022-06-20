#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except IndexError as e:
        sys.stderr.write("Except: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
    except TypeError as e:
        sys.stderr.write("Except: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
    except ValueError as e:
        sys.stderr.write("Except: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
    except ZeroDivisionError as e:
        sys.stderr.write("Except: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
