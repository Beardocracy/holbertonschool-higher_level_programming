#!/usr/bin/python3
''' This module tests the rectangle class '''
import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    ''' This is a unittest for class rectangle '''
    def setUp(self):
        ''' Resets the class variable'''
        Base._Base__nb_objects = 0
    
    def test_type(self):
        ''' Tests if type is correct '''
        a = Rectangle(5, 5)
        self.assertEqual(type(a), Rectangle)

    def test_id_assignment(self):
        ''' Tests if id assignment works '''
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 5, 0, 0, 98)
        self.assertEqual(r2.id, 98)
        r3 = Rectangle(10, 5, 0, 0)
        self.assertEqual(r3.id, 2)

    def test_hwxy_assignment(self):
        ''' tests to see if variable assignment works '''
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
        ''' tests for input validation exceptions and messages'''
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

    def test_area(self):
        ''' Tests for correct output of area method '''
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.area(), 50)
        r2 = Rectangle(5, 5, 1, 1)
        self.assertEqual(r2.area(), 25)

    def test_display(self):
        ''' Tests for correct output of display method '''
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(2, 3, 2, 2)
        r4 = Rectangle(3, 2, 1, 0)
        orig_stdout = sys.stdout
        with open('test_rectangle.txt', 'w') as f:
            sys.stdout = f
            r1.display()
        with open('test_rectangle.txt', 'r') as f:
            self.assertEqual(f.read(), '###\n###\n')
        with open('test_rectangle.txt', 'w') as f:
            sys.stdout = f
            r2.display()
        with open('test_rectangle.txt', 'r') as f:
            self.assertEqual(f.read(), '##\n##\n##\n##\n')
        with open('test_rectangle.txt', 'w') as f:
            sys.stdout = f
            r3.display()
        with open('test_rectangle.txt', 'r') as f:
            self.assertEqual(f.read(), '\n\n  ##\n  ##\n  ##\n')
        with open('test_rectangle.txt', 'w') as f:
            sys.stdout = f
            r4.display()
        with open('test_rectangle.txt', 'r') as f:
            self.assertEqual(f.read(), ' ###\n ###\n')
        sys.stdout = orig_stdout

    def test_str(self):
        ''' Tests the __str__ method override '''
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        orig_stdout = sys.stdout
        with open('test_rectangle.txt', 'w') as f:
            sys.stdout = f
            print(r1)
        with open('test_rectangle.txt', 'r') as f:
            self.assertEqual(f.read(), '[Rectangle] (12) 2/1 - 4/6\n')
        with open('test_rectangle.txt', 'w') as f:
            sys.stdout = f
            print(r2)
        with open('test_rectangle.txt', 'r') as f:
            self.assertEqual(f.read(), '[Rectangle] (1) 1/0 - 5/5\n')
        sys.stdout = orig_stdout

