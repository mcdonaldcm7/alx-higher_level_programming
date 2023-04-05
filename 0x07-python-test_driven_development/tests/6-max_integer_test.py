#!/usr/bin/python3
"""
This module contains tests for the 6-max_integer module, it tests the
max_integer function and makes sure the requirements are met
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A test class for the MaxInteger class created for the max_integer function
    """
    def test_max_integer(self):
        numbers = [4, 2, -1, 3, 5, 6]
        self.assertEqual(max_integer(numbers), 6)
        numbers = [9]
        self.assertEqual(max_integer(numbers), 9)
        self.assertEqual(max_integer([]), None)
