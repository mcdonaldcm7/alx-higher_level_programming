#!/usr/bin/python3
def print_last_digit(number):
    last = 0 if ((abs(number) % 10) == 0) else (
            abs(number) % 10)
    print("{0:d}".format(last), end="")
    return (last)
