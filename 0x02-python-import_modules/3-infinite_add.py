#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    add = 0
    for i in range(1, argc):
        add += int(argv[i])
    print("{0:d}".format(add))
