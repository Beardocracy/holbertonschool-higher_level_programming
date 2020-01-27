#!/usr/bin/python3
''' This module contains the class rectangle '''
from models.base import Base


class Rectangle(Base):
    ''' This is the class rectangle which inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Class constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' Returns the width '''
        return self.__width

    @width.setter
    def width(self, width):
        ''' Sets the width, with validation '''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        ''' Returns the height '''
        return self.__height

    @height.setter
    def height(self, height):
        ''' Sets the height, with validation '''
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        ''' Gets the x '''
        return self.__x

    @x.setter
    def x(self, x):
        ''' Sets the x, with validation '''
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        ''' Gets the y '''
        return self.__y

    @y.setter
    def y(self, y):
        ''' Sets the y with validation '''
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        ''' Returns the area of the rectangle '''
        return self.width * self.height

    def display(self):
        ''' Prints in stdout the instance with char # '''
        rows = self.width
        cols = self.height
        for y in range(self.y):
            print()
        for c in range(cols):
            for x in range(self.x):
                print(' ', end='')
            for r in range(rows):
                print('#', end='')
            print()

    def __str__(self):
        ''' Overrides the str method '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        ''' Updates an existing instance '''
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]
        if num_args == 0:
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        ''' Returns the dictionary representation of the instance '''
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x':
                self.x, 'y': self.y}
