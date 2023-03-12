#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_a = 0
    t_b = 0
    if len(tuple_a) > 0:
        t_a += tuple_a[0]
    if len(tuple_b) > 0:
        t_a += tuple_b[0]
    if len(tuple_a) > 1:
        t_b += tuple_a[1]
    if len(tuple_b) > 1:
        t_b += tuple_b[1]
    return ((t_a, t_b))
