#!/usr/bin/python3


def number_of_lines(filename=""):
    ''' Returns the number of lines in a text file'''
    numb_lines = 0
    with open(filename, 'r') as f:
        for line in f:
            numb_lines += 1
    return numb_lines
