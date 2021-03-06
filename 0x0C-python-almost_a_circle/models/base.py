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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Converts dictionary object to json '''
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the json representation of list_objs to file '''
        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        filename = cls.__name__ + '.json'
        list_dicts = []
        for each in list_objs:
            list_dicts.append(each.to_dictionary())
        json_list = Base.to_json_string(list_dicts)
        with open(filename, "w") as f:
            f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the json string representation json_string '''
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Creates an instance from a dictionary '''
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances from file '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except:
            return []
        list_dicts = cls.from_json_string(json_string)
        list_objs = []
        for each in list_dicts:
            list_objs.append(cls.create(**each))
        return list_objs
