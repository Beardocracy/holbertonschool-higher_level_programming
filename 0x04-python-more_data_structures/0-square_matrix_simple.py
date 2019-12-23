#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    squares = [[x * x for x in y] for y in matrix]
    return squares
