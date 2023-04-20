#!/usr/bin/python3

import unittest
import sys
import io
import json
import os
sys.path.append('../')
sys.path.append('models')
Rectangle = __import__('rectangle').Rectangle

class TestRectangle(unittest.TestCase):


    def test_rectangle(self):
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

    def test_rectangle_display(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rectangle = Rectangle(1, 2)
        rectangle.display()
        sys.stdout = sys.__stdout__
        display = "#\n#\n"
        self.assertEqual(captured_output.getvalue(), display)

    def test_rectangle_display1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rectangle = Rectangle(1, 2, 1)
        rectangle.display()
        sys.stdout = sys.__stdout__
        display = " #\n #\n"
        self.assertEqual(captured_output.getvalue(), display)

    def test_rectangle_display2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rectangle = Rectangle(1, 2, 1, 1)
        rectangle.display()
        sys.stdout = sys.__stdout__
        display = "\n #\n #\n"
        self.assertEqual(captured_output.getvalue(), display)

    def test_rectangle_to_dictionary(self):
        rectangle = Rectangle(1, 2, id = 1)
        dictionary = rectangle.to_dictionary()
        expected_dict = {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 1}
        self.assertEqual(dictionary, expected_dict)

    def test_rectangle_update(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        rectangle.update(89)
        self.assertEqual(rectangle.id, 89)

    def test_rectangle_update1(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        rectangle.update(89, 3)
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 3)

    def test_rectangle_update2(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        rectangle.update(89, 4, 6)
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 6)

    def test_rectangle_update3(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        rectangle.update(89, 5, 6, 3)
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 3)

    def test_rectangle_update4(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        rectangle.update(89, 6, 7, 4, 5)
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_rectangle_update_kwarg(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        kwargs = {"id": 72}
        rectangle.update(**kwargs)
        self.assertEqual(rectangle.id, 72)

    def test_rectangle_update_kwarg1(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        kwargs = {"id": 73, "width": 8}
        rectangle.update(**kwargs)
        self.assertEqual(rectangle.id, 73)
        self.assertEqual(rectangle.width, 8)

    def test_rectangle_update_kwarg2(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        kwargs = {"id": 22, "width": 5, "height": 7}
        rectangle.update(**kwargs)
        self.assertEqual(rectangle.id, 22)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 7)

    def test_rectangle_update_kwarg3(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        kwargs = {"id": 22, "width": 5, "height": 7, "x": 5}
        rectangle.update(**kwargs)
        self.assertEqual(rectangle.id, 22)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 5)

    def test_rectangle_update_kwarg4(self):
        rectangle = Rectangle(1, 2, id=2)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        kwargs = {"id": 22, "width": 5, "height": 7, "x": 5, "y": 10}
        rectangle.update(**kwargs)
        self.assertEqual(rectangle.id, 22)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 10)

    def test_rectangle_create(self):
        dictionary = {"id" : 89}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 89)

    def test_rectangle_create1(self):
        dictionary = {"id" : 89, "width": 42}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 42)

    def test_rectangle_create2(self):
        dictionary = {"id" : 89, "width": 42, "height": 13}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 42)
        self.assertEqual(rec.height, 13)

    def test_rectangle_create3(self):
        dictionary = {"id" : 89, "width": 42, "height": 13, "x": 3}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 42)
        self.assertEqual(rec.height, 13)
        self.assertEqual(rec.x, 3)

    def test_rectangle_create4(self):
        dictionary = {"id" : 89, "width": 42, "height": 13, "x": 3, "y": 4}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 42)
        self.assertEqual(rec.height, 13)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)

    def test_rectangle_save_to_file(self):
        Rectangle.save_to_file(None)
        filename = "Rectangle.json"
        json_repr = None
        expected_repr = "[]"
        with open(filename, "r") as f:
            json_repr = f.read()
        self.assertEqual(json_repr, expected_repr)

    def test_rectangle_save_to_file2(self):
        Rectangle.save_to_file([])
        filename = "Rectangle.json"
        json_repr = None
        expected_repr = "[]"
        with open(filename, "r") as f:
            json_repr = f.read()
        self.assertEqual(json_repr, expected_repr)

    def test_rectangle_save_to_file3(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        filename = "Rectangle.json"
        json_repr = None
        with open(filename, "r") as f:
            json_repr = f.read()
        rect = Rectangle(5, 5)
        dictionary = json.loads(json_repr)[0]
        rect.update(**dictionary)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_load_from_file(self):
        if not os.path.exists('Rectangle.json'):
            list_obj = Rectangle.load_from_file()
            self.assertIsInstance(list_obj, list)
            self.assertEqual(list_obj, [])

    def test_rectangle_load_from_file2(self):
        if os.path.exists('Rectangle.json'):
            list_obj = Rectangle.load_from_file()
            self.assertIsInstance(list_obj, list)
            for obj in list_obj:
                self.assertIsInstance
