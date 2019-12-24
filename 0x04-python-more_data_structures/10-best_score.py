#!/usr/bin/python3


def best_score(a_dictionary):
    bigKey = None
    bigNum = 0
    if type(a_dictionary) == dict:
        for key in a_dictionary:
            if a_dictionary[key] > bigNum:
                bigNum = a_dictionary[key]
                bigKey = key
    return bigKey
