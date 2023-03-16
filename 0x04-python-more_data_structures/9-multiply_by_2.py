#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret = {}
    if a_dictionary is None:
        return
    for k in a_dictionary:
        ret[k] = (a_dictionary[k] * 2)
    return (ret)
