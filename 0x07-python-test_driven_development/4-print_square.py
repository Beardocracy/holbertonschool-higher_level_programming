#!/usr/bin/python3
'''
This module contains a tested square printing function
Test can be found in 'tests/'
'''


def print_square(size):
    """ Prints a square of #s
    Args:
        size (int): the size of the square. Must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for n in range(size):
        for m in range(size):
            print("#", end="")
        print()
