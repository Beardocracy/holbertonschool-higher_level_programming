#!/usr/bin/python3
''' This module contains the class Base '''
import json


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

    def to_json_string(list_dictionaries):
        ''' Converts dictionary object to json '''
        if list_dictionaries is None:
            return "[]"
        if not bool(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)
