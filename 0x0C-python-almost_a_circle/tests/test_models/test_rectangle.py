#!/usr/bin/python3
"""
    unittest for rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        class for testing TestRectangle
    """
    def testRectangle(self):
        self.assertTrue(issubclass(Rectangle, Base))

        r1 = Rectangle(10, 2)
        self.assertTrue(r1.width == 10 and r1.height == 2)

        r2 = Rectangle(2, 10)
        self.assertTrue(r2.width == 2 and r2.height == 10)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertTrue(r3.width == 10 and r3.height == 2)
        self.assertTrue(r3.x == 0 and r3.y == 0)
        r3.width = 13
        r3.height = 5
        r3.x = 1
        r3.y = 4
        self.assertTrue(r3.width == 13 and r3.height == 5 and r3.x == 1 and r3.y == 4)
