#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            U = chr(ord(c) - 32)
        else:
            U = c
        print("{}".format(U), end="")
    print()
