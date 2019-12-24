#!/usr/bin/python3
def roman_to_int(roman_string):
    romNums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    if type(roman_string) == str:
        length = len(roman_string)
        for n in range(length):
            if n == length - 1:
                total += romNums[roman_string[n]]
                return total
            elif romNums[roman_string[n]] < romNums[roman_string[n + 1]]:
                total -= romNums[roman_string[n]]
            else:
                total += romNums[roman_string[n]]
    return total
