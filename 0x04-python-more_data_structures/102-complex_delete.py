#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return
    rm = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            rm.append(i)
    for i in rm:
        del(a_dictionary[i])
    return (a_dictionary)
