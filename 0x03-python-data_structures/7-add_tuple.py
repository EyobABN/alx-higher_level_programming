#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ints = [0, 0]
    for i in range(2):
        a = tuple_a[i] if i <= len(tuple_a) - 1 else 0
        b = tuple_b[i] if i <= len(tuple_b) - 1 else 0
        ints[i] = a + b
    return (ints[0], ints[1])
