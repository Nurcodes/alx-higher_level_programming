#!/usr/bin/python3

"""This module defines a function
    which divides all elements of of a matrix
    by a given int"""


def matrix_divided(matrix, div):
    """Divides a 2d matrix
        by a given number
        Args: matrix(2dmatrix), div(int)"""
    flag = False
    first = "matrix must be a matrix "
    second = "(list of lists) of integers/floats"

    for i in matrix:
        if matrix is not None:
            for j in i:
                if not isinstance(j, int) and not isinstance(j, float):
                    flag = True
                    break
        else:
            raise(TypeError("{}{}".format(first, second)))
    if flag:
        raise TypeError("{}{}".format(first, second))

    rs = []
    for row in matrix:
        rs.append(len(row))
    first = rs[0]
    result = True
    for i in rs:
        if first != i:
            result = False
            break
        else:
            continue
    if not result:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [item[:] for item in matrix]
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = round(new[i][j] / div, 2)
    return new
