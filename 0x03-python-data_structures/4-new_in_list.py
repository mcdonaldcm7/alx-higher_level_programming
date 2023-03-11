#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    size = len(my_list)
    if (idx < 0) or (idx > (size - 1) and size != 0):
        return (None)
    copy = my_list.copy()
    if size == 0:
        copy.append(element)
    else:
        copy[idx] = element
    return (copy)
