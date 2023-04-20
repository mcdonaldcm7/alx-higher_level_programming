#!/usr/bin/python3

import unittest
import sys
sys.path.append('../')
sys.path.append('models')
Base = __import__('base').Base

class TestBase(unittest.TestCase):

    def test_init(self):
        test_base = Base()
        test_base2 = Base()
        test_base3 = Base(89)
        self.assertEqual(test_base.id, 1)
        self.assertEqual(test_base2.id, 2)
        self.assertEqual(test_base3.id, 89)
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string,
        "[{\"x\": 2, \"width\": 10, \"id\": 1, \"height\": 7, \"y\": 8}]")
        self.assertIsInstance(json_string, str)
