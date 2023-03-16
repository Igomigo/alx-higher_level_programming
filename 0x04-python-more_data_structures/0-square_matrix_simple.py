#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = []
    for m in matrix:
        new_mat.append(list(map(lambda x: x ** 2, m)))
    return new_mat
