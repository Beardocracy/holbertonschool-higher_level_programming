#!/usr/bin/python3
'''
This module contains an addition function (test-proven).
'''

def add_integer(a, b=98):
    """ Adds two numbers
    If a float is passed, it will be cast to an int
    Args:
        a (int): the first number
        b (int): the second number (optional)
    Returns:
        int: the sum of the two values
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')

    return a + b
