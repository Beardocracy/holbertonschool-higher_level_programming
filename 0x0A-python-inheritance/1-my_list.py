#!/usr/bin/python3


class MyList(list):
    
    def print_sorted(self):
        '''
        Prints a list of integers in order
        '''
        o_list = self[:]
        o_list.sort()
        print(o_list)
