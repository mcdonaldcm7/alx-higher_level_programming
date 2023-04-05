#!/usr/bin/python3
"""
This module contains the definition for the matrix_divided function which
divides all the elements of a matrix by the given divisor
"""


def matrix_divided(matrix, div):
    """
    This function simply divides all the element of a matrix by the specified
    div integer. div has to be an integer or a float with value not equal to
    zero

    Parameter(s)
    ------------
    matrix (list): A list of lists representing the rows of the matrix
    div (int): The divisor for the elements of the array

    Returns: A new array with the divided elements
    """
    for r in matrix:
        if not (all((isinstance(i, int) or isinstance(i, float))
                    for i in r)):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    for r in matrix:
        if len(r) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ret = []
    for i in range(len(matrix)):
        ret.append([])
        for j in matrix[i]:
            ret[i].append(round(j / div, 2))
    return (ret)
