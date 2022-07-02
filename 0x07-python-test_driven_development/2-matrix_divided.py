#!/usr/bin/python3

"""This module defines a function
    which divides all elements of of a matrix
    by a given int"""


def matrix_divided(matrix, div):
    """Divides a 2d matrix
        by a given number
        Args: matrix(2dmatrix), div(int)
        """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix[0]) not in [list]:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row]
                  for row in matrix]
    return new_matrix
