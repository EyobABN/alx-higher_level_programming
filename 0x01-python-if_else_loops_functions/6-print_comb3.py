#!/usr/bin/python3
separator = ""
for i in range(10):
    for j in range(10):
        if (i < j):
            print(separator, "{}{}".format(i, j), sep="", end="")
            separator = ", "
print()
