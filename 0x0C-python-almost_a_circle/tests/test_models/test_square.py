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

    def test_update(self):
        ''' Tests the update method '''
        s1 = Square(10, 10, 10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(89, 2, size=5)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        s1.update(89, 2, 3)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        s1.update(89, 2, 3, 4, id=98)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        s1.update(size=1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_dictionary(self):
        ''' Tests the dictionary method and using it with update method '''
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        control_dict = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(s1_dict, control_dict)
        self.assertEqual(type(s1_dict),  dict)
        s2 = Square(1, 1)
        s2_dict = s2.to_dictionary()
        self.assertEqual(str(s2), '[Square] (2) 1/0 - 1')
        s2.update(**s1_dict)
        self.assertEqual(str(s2), '[Square] (1) 2/1 - 10')

