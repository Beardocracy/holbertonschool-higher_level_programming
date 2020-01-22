#!/usr/bin/python3


def write_file(filename="", text=""):
    ''' Writes a string to a text file'''
    with open(filename, 'w') as f:
        chars_written = f.write(text)
    return chars_written
