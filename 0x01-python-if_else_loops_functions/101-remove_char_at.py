#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newString = ''
    for c in str:
        if n != i:
            newString += c
        i += 1
    return newString
