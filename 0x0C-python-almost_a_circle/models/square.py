#!/usr/bin/python3
''' This module contains the description for class square '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square inherits from Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Square is a rectangle with the same width and height '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Overrides the str method '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        ''' Sets the size, with validation '''
        if type(size) is not int:
            raise TypeError('width must be an integer')
        elif size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size
