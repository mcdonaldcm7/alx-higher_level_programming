#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = []
    for num in my_list:
        if (num % 2) == 0:
            ret.append(True)
        else:
            ret.append(False)
    return (ret)
