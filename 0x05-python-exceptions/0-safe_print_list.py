#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    r = 0
    for i in range(x):
        try:
            print("{0}".format(my_list[i]), end="")
            r += 1
        except IndexError:
            print()
            return (i)
    print()
    return (r)
