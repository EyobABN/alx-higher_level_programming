#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
digit = round(math.fmod(number, 10))
if digit > 5:
    place = "greater than 5"
elif digit == 0:
    place = "0"
else:
    place = "less than 6 and not 0"
print(f"Last digit of {number} is {digit} and is {place}")
