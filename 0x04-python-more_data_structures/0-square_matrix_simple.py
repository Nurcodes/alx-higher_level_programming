#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for i in matrix:
        a.append(list(map(lambda a: (a ** 2), i)))
    return a
