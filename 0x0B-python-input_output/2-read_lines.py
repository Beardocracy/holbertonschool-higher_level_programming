#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    numb_printed = 0
    with open(filename, 'r') as f:
        for line in f:
            if nb_lines < 1 or numb_printed < nb_lines:
                print(line, end="")
                numb_printed += 1
