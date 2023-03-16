#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (a_dictionary)
    key = None
    for k in a_dictionary:
        if (key is None):
            key = k
        if a_dictionary[k] > a_dictionary[key]:
            key = k
    return (key)
