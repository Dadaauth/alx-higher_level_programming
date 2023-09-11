#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(13)
        self.b4 = Base()
        self.b5 = Base(20)
        self.b6 = Base()

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 13)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, 20)
        self.assertEqual(self.b6.id, 4)

if __name__ == "__main__":
    unittest.main()
