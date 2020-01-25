#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        ''' Resets the class variable'''
        Base._Base__nb_objects = 0
    
    def test_type(self):
        a = Rectangle(5, 5)
        self.assertEqual(type(a), Rectangle)

    def test_id_assignment(self):
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 5, 0, 0, 98)
        self.assertEqual(r2.id, 98)
        r3 = Rectangle(10, 5, 0, 0)
        self.assertEqual(r3.id, 2)

    def test_hwxy_assignment(self):
        r1 = Rectangle(10, 5, 3, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        r2 = Rectangle(1, 5)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_input_validation(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1 = Rectangle('hi', 5)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r2 = Rectangle(5, 'hi')
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r3 = Rectangle(5, 5, 'hi', 5)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r4 = Rectangle(5, 5, 0, 'hi')
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r5 = Rectangle(-5, 5)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r6 = Rectangle(5, -5)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r7 = Rectangle(5, 5, -1, 5)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r8 = Rectangle(5, 5, 5, -5)

