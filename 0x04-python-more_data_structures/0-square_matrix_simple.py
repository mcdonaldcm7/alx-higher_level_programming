#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[i])):
            tmp.append(matrix[i][j]**2)
        r.append(tmp)
    return (r)
