#!/usr/bin/python3
"""This module contains a class that inherits everything from 'list' and adds a
function that prints a sorted list."""


class MyList(list):
    def print_sorted(self):
        '''Prints a list in ascending order'''
        print(sorted(self))
