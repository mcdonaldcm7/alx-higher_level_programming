#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    if (argc - 1) == 0:
        print("0 arguments.")
    elif (argc - 1) == 1:
        print("1 argument:\n1: {0}".format(argv[1]))
    else:
        print("{0:d} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{0:d}: {1:s}".format(i, argv[i]))
