#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 15) == 0:
            print("FizzBuzz", end=("\n" if i == 100 else " "))
        elif (i % 5) == 0:
            print("Buzz", end=("\n" if i == 100 else " "))
        elif (i % 3) == 0:
            print("Fizz", end=("\n" if i == 100 else " "))
        else:
            print("{0}".format(i), end=("\n" if i == 100 else " "))
