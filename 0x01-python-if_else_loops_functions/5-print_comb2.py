#!/usr/bin/python3
separator = ""
for i in range(100):
    print(separator, "{:02d}".format(i), end="", sep="")
    separator = ", "
print()
