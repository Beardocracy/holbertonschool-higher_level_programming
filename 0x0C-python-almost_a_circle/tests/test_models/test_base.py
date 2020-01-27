#!/usr/bin/python3
''' Module for testing the Base class'''
import unittest
import json
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

    def test_save_to_file(self):
        ''' Tests the save to file method '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_dicts_from_file = []
        with open("Rectangle.json", "r") as f:
            list_dicts_from_file = json.loads(f.read())
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(list_dicts, list_dicts_from_file)

    def test_from_json(self):
        ''' Tests the from_json_string method '''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, list_input)

    def test_create(self):
        ''' Tests the create method '''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        ''' Tests the load from file method '''

