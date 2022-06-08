#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    roman = {
            'I': 1, 'i': 1,
            'V': 5, 'v': 5,
            'X': 10, 'x': 10,
            'L': 50, 'l': 50,
            'C': 100, 'c': 100,
            'D': 500, 'd': 500,
            'M': 1000, 'm': 1000
            }
    total = 0
    for i in range(len(roman_string)):
        num = roman.get(roman_string[i])
        if i != len(roman_string) - 1:
            nxt_num = roman.get(roman_string[i + 1])
        else:
            nxt_num = 0
        if num < nxt_num:
            num = num * (-1)
        total += num
    return total
