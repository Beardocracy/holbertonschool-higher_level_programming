#!/usr/bin/python3
'''
This module contains a tested function for dividing matrixes
'''


def matrix_divided(matrix, div):
    """ Divides all the elements of a matrix
    Args:
        matrix (list of lists): integers or floats only
        div (int or float): The number to divide each element in matrix.
                            Can't be zero.
    Return:
        New matrix.
    """
    e_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError(e_matrix)

    try:
        list_length = len(matrix[0])
    except TypeError:
        raise TypeError(e_matrix)

    new_matrix = []

    for each_list in matrix:
        if not isinstance(each_list, list):
            raise TypeError(e_matrix)
        elif len(each_list) != list_length:
            raise TypeError('Each row of the matrix must have the same size')
        new_sublist = []
        for value in each_list:
            if not isinstance(value, (int, float)):
                raise TypeError(e_matrix)
            new_sublist.append(round(value / div, 2))
        new_matrix.append(new_sublist)
    return new_matrix
