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

    def test_ids(self):
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertequal(self.r3.id, 12)
