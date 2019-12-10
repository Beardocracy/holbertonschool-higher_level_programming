#!/usr/bin/python3
def uppercase(str):
    for i in str:
        tempChar = ord(i)
        if tempChar >= ord('a') and tempChar <= ord('z'):
            tempChar -= 32
        print('{:c}'.format(tempChar), end='')
    print('')
