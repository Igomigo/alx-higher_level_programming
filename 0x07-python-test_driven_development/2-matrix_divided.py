#!/usr/bin/python3
"""
A module containing a function(matrix_divided(matrix, div)
which takes two arguments and returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    the matrix function that divides all elements in a matrix
    and returns a new matrix.

    args:
        matrix: the matrix itself (a list of lists).
        div: the divisor, must not be (0).

    returns:
        A new matrix containing the already divided elements.
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(i, (int, float))
                       for row in matrix for i in row):
        raise TypeError(error)

    row_length = len(matrix[0])
    # To get the length of the first row

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
