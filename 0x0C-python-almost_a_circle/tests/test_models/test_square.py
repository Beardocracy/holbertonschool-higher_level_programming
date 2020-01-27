#!/usr/bin/python3
''' This module has the unittest for the class square '''
import unittest
import sys
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_square(unittest.TestCase):
    ''' This is a unittest for class square '''
    def setUp(self):
        ''' Resets the class variable'''
        Base._Base__nb_objects = 0

    def test_type(self):
        ''' Tests if type is correct '''
        a = Square(5)
        self.assertEqual(type(a), Square)
        b = Square(5, 1, 1)
        self.assertEqual(type(b), Square)
    
    def test_str(self):
        ''' Tests the __str__ method override '''
        r1 = Square(5, 2, 1, 12)
        r2 = Square(5, 5, 1)
        r3 = Square(7)
        self.assertEqual(str(r1), '[Square] (12) 2/1 - 5')
        self.assertEqual(str(r2), '[Square] (1) 5/1 - 5')
        self.assertEqual(str(r3), '[Square] (2) 0/0 - 7')

    def test_validation(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')
        s1.size = 10
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 10')
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1.size = "string_cheese"
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.size = -89


