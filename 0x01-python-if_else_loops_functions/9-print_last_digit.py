#!/usr/bin/python3
def print_last_digit(number):
    last = (abs(number) % 10) * abs(number) / number
    print("{0}".format(last))
    return (last)
