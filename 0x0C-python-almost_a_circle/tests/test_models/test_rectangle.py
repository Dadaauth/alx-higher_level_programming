#!/usr/bin/python3
"""
the testing module for the rectangle file
"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    the test case class to test the rectangle class
    """
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3

    def test_a_ids(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_errors(self):
        self.assertRaises(TypeError, Rectangle, ("11", 12, 3, 4))
        self.assertRaises(TypeError, Rectangle, (11, "23", 3, 4))
        self.assertRaises(TypeError, Rectangle, (11, 3, {1, 3}, 4))
        self.assertRaises(TypeError, Rectangle, (11, 12, 3, "dd"))

    def test_v_error(self):
        self.assertRaises(ValueError, Rectangle, -1, 2, 3, 3)
        self.assertRaises(ValueError, Rectangle, 1, -2, 3, 3)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3, 3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -3)

    def test_area(self):
        self.assertEqual(self.r2.area(), 20)
