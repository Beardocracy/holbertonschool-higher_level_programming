#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        if isinstance(value, tuple) is False or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif isinstance(value[0], int) is False:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif isinstance(value[1], int) is False:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            x = self.__position[0]
            y = self.__position[1]
            for yax in range(y):
                print()
            for i in range(self.__size):
                for k in range(x):
                    print(end=" ")
                for j in range(self.__size):
                    print("#", end="")
                print()
