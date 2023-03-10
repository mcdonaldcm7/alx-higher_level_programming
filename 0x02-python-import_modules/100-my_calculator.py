#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import exit, argv

a = int(argv[1])
b = int(argv[3])


def result(opr):
    if opr == '+':
        return (add(a, b))
    elif opr == '-':
        return (sub(a, b))
    elif opr == '*':
        return (mul(a, b))
    elif opr == '/':
        return (div(a, b))
    return (None)


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)
    print("{0:d} {2:s} {1:d} = {3:d}".format(a, b, argv[2], result(argv[2])))
