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
    
    def update(self, *args, **kwargs):
        ''' Updates an existing instance '''
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.size = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]
        if num_args == 0:
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        ''' Returns the dictionary representation of the instance '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
