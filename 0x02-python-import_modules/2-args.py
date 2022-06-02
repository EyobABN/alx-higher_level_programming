#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    if n == 1:
        s = "argument"
    else:
        s = "arguments"
    if n == 0:
        c = "."
    else:
        c = ":"
    print("{} {}{}".format(n, s, c))
    for i in range(1, n + 1):
        print("{}: {}".format(i, argv[i]))
