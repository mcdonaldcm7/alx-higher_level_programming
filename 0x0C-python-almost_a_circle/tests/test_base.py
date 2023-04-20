#!/usr/bin/python3

import unittest
import sys
sys.path.append('../')
sys.path.append('models')
Base = __import__('base').Base
Rectangle = __import__('rectangle').Rectangle

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

    def test_rectagle(self):
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_x(self):
        rectangle = Rectangle(1, 2, 3)
        self.assertEqual(rectangle.x, 3)

    def test_rectangle_y(self):
        rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_init_error(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_init_error2(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_init_error3(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_init_error4(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_init_id(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.id, 5)

    def test_rectangle_val_excpt(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_val_excpt1(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_val_excpt2(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_val_excpt3(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_val_excpt4(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_val_excpt5(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        rectangle = Rectangle(2, 10)
        self.assertEqual(rectangle.area(), 20)

    def test_rectangle_str(self):
        rectangle = Rectangle(1, 2, id=1)
        string = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(rectangle.__str__(), string)
