#!/usr/bin/python3


class MyList(list):
    
    def print_sorted(self):
        '''
        Prints a list of integers in order
        '''
        sorted_list = list(set(self))
        print(sorted_list)
