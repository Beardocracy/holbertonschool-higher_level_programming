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
