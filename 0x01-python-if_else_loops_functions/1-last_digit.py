#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0 if number == 0 else (abs(number) % 10) * (abs(number) // number)
if (number % 10) > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif (number % 10) == 0:
    print(f"Last digit of {number:d} is {last:d} and is is 0")
else:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
