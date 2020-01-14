#!/usr/bin/python3
'''
This module contains a tested function
Tests can be found in 'tests/'
'''


def text_indentation(text):
    """ Prints a text with 2 new lines after each .,?
    Args:
        text (string): the text to be printed.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    length = len(text)
    i = 0
    while i < length:
        if text[i] in ":.?":
            print("{}\n".format(text[i]))
            i += 1
            while i < length and text[i] == " ":
                i += 1
        if i < length:
            print("{}".format(text[i]), end="")
        i += 1
