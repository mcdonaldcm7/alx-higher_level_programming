#!/usr/bin/python3
def uniq_add(my_list=[]):
    r = set()
    for i in range(len(my_list)):
        r.add(my_list[i])
    add = 0
    for i in r:
        add += i
    return (add)
