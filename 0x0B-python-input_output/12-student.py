#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        bd = self.__dict__
        if attrs is None:
            return bd
        new = {}
        for item in attrs:
            if item in bd.keys():
                new.update({item: bd.get(item)})
        return new
