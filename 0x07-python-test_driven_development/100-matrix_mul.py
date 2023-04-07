#!/usr/bin/python3
"""
This module contains the definition for the matrix_mul method which returns
the product of multiplying two matrices together.
It also contains type checks to ensure that each of the matrices passed
contains only integer or float values, they're not empty, the dimension
prerequisite for a matrix multiplication has been met, and so on.
"""


def matrix_mul(m_a, m_b):
    """
    This function multiplies and returns the product of two matrices created
    using multidimentional lists.

    Paramete(s)
    -----------
    m_a (list): First matrix
    m_b (list): Second matrix

    Returns:
        m_a * m_b
    """
    el_a = [0, 0]
    el_b = [0, 0]
    m_c = []
    row = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    mx_row_a = len(m_a)
    mx_row_b = len(m_b)
    if mx_row_a == 0:
        raise ValueError("m_a can't be empty")
    if mx_row_b == 0:
        raise ValueError("m_b can't be empty")
    mx_col_a = len(m_a[0])
    mx_col_b = len(m_b[0])
    if mx_col_a == 0:
        raise ValueError("m_a can't be empty")
    if mx_col_b == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_b should contain only integers or floats")
    for i in m_a:
        if len(i) != mx_col_a:
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if len(i) != mx_col_b:
            raise TypeError("each row of m_b must be of the same size")
    if mx_col_a != mx_row_b:
        raise ValueError("m_a and m_b can't be multiplied")
    for rows in range(mx_row_a):
        for cols in range(mx_col_b):
            elem = 0
            for e in range(mx_col_a):
                v_a = m_a[el_a[0]][el_a[1]]
                v_b = m_b[el_b[0]][el_b[1]]
                elem += v_a * v_b
                el_a[1] += 1
                el_b[0] += 1
            row.append(elem)
            if (el_b[1] + 1) >= mx_col_b:
                el_b[1] = 0
            else:
                el_b[1] += 1
            el_a[1] = 0
            el_b[0] = 0
        m_c.append(row)
        row = []
        if (el_a[0] + 1) >= mx_row_a:
            el_a[0] = 0
        else:
            el_a[0] += 1
        el_b[1] = 0
    return (m_c)
