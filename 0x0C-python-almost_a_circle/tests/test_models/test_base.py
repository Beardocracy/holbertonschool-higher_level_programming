#!/usr/bin/python3
''' Module for testing the Base class'''
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    
    def setUp(self):
        ''' Resets the class variable'''
        Base._Base__nb_objects = 0

    def test_initialization(self):
        new = Base()
        self.assertEqual(type(new), Base)

    def test_id_assignment(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(98)
        self.assertEqual(b.id, 98)
        c = Base()
        self.assertEqual(c.id, 2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        empty = {}
        self.assertEqual(Base.to_json_string(empty), "[]")
