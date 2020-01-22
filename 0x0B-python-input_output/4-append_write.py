#!/usr/bin/python3


def append_write(filename="", text=""):
    ''' appends a string at the end of a text file '''
    with open(filename, 'a') as f:
        char_written = f.write(text)
    return char_written
