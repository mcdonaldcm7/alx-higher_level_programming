#!/usr/bin/python3
for i in range(122, 96, -1):
    asc = 0
    if (i % 2) == 0:
        asc = i
    else:
        asc = i - 32
    print("{0}".format(chr(asc)), end="")
