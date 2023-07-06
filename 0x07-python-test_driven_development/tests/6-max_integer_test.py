#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_values(self):
        self.assertEqual(max_integer([1, 4, 5, 7, -10]), 7)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0, 0, 0, 19, 2000000, -100]), 2000000)
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-12]), -12)
