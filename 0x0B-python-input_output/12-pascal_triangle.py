#!/usr/bin/python3
"""
This module contains the definition for the 'pascal_triangle' function which
returns a list of lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n
    """

    if n <= 0:
        return ([])
    
    triangle = []
    for curr_index in range(n):
        new_index = []
        if curr_index == 0:
            new_index.append(1)
        else:
            prev_index = triangle[curr_index - 1]
            for i in range(curr_index + 1):
                if i == 0 or i >= len(prev_index):
                    new_index.append(1)
                else:
                    new_index.append(prev_index[i] + prev_index[i - 1])
        triangle.append(new_index)
    return (triangle)

