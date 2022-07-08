#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        class for testing max_integer
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)
        self.assertEqual(max_integer([2, -1, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
