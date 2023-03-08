#!/usr/bin/python3
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        if i == j:
            continue
        if j < i:
            continue
        print("{0}{1}".format(i, j),
              end=("\n" if i == 8 and j == 9 else ", "))
