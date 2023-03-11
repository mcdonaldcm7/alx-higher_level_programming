#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    first = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j:
                print(" ", end="")
            print("{0:d}".format(matrix[i][j]), end="")
        print("$")
