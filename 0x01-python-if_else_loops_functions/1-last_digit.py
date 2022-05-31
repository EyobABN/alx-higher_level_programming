#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit > 5:
    place = "greater than 5"
elif digit == 0:
    place = "zero"
else:
    place = "less than 6 and not 0"
print(f"Last digit of {number} is {digit} and is {place}")
