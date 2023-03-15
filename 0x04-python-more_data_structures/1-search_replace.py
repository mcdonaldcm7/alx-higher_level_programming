#!/usr/bin/python3
def search_replace(my_list, search, replace):
    r = []
    for i in range(len(my_list)):
        if my_list[i] == search:
             r.append(replace)
        else:
            r.append(my_list[i])
    return (r)
