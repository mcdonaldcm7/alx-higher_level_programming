#!/usr/bin/python3

import unittest
import sys
sys.path.append('../')
sys.path.append('models')
Base = __import__('base').Base

class TestBase(unittest.TestCase):

    
    def test_init(self):
        test_base = Base()
        self.assertEqual(test_base.id, 1)

    def test_init_increment(self):
        test_base2 = Base()
        self.assertEqual(test_base2.id, 2)

    def test_id_save(self):
        test_base3 = Base(89)
        self.assertEqual(test_base3.id, 89)

    def test_base_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_dic(self):
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string,
        "[{\"x\": 2, \"width\": 10, \"id\": 1, \"height\": 7, \"y\": 8}]")
        self.assertIsInstance(json_string, str)

    def test_from_json_string_none(self):
        ret = Base.from_json_string(None)
        self.assertEqual(ret, [])

    def test_from_json_string_empty(self):
        ret = Base.from_json_string("[]")
        self.assertEqual(ret, [])

    def test_from_json_string_dict(self):
        ret = Base.from_json_string("[{\"id\": 89}]")
        self.assertEqual(ret[0]["id"], 89)

    def test_from_json_string_return(self):
        ret = Base.from_json_string(None)
        self.assertIsInstance(ret, list)
