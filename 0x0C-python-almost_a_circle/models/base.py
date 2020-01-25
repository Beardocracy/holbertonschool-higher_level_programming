#!/usr/bin/python3
''' This module contains the class Base '''

class Base:
    ''' This is the definition for the base object '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' This is the first thing that runs when you create an instance '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
