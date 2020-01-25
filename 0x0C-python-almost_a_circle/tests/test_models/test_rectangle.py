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

