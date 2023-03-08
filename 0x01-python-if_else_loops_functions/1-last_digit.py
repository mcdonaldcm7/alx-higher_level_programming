#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt = 0
if (abs(number) % 10) == 0:
    lt = 0
else:
    lt = (abs(number) % 10) * (abs(number) // number)
if (number % 10) > 5:
    print(f"Last digit of {number:d} is {lt:d} and is greater than 5")
elif (number % 10) == 0:
    print(f"Last digit of {number:d} is {lt:d} and is is 0")
else:
    print(f"Last digit of {number:d} is {lt:d} and is less than 6 and not 0")
