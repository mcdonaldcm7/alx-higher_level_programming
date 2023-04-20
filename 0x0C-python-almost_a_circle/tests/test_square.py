#!/usr/bin/python3

import unittest
import sys
import io
import json
import os
sys.path.append('../')
sys.path.append('models')
Square = __import__('square').Square

class TestSquare(unittest.TestCase):


    def test_square(self):
        square = Square(1, id=1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)

    def test_square_x(self):
        square = Square(1, 3)
        self.assertEqual(square.x, 3)

    def test_square_y(self):
        square = Square(1, 3, 4)
        self.assertEqual(square.y, 4)

    def test_square_init_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_init_error2(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_init_error3(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_init_error4(self):
        with self.assertRaises(TypeError):
            Square(1, "2", 3)

    def test_square_init_id(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.id, 4)

    def test_square_val_excpt(self):
        with self.assertRaises(ValueError):
            Square(-2)

    def test_square_val_excpt1(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_val_excpt2(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_val_excpt3(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_area(self):
        square = Square(10)
        self.assertEqual(square.area(), 100)

    def test_square_str(self):
        square = Square(1, id=1)
        string = "[Square] (1) 0/0 - 1"
        self.assertEqual(square.__str__(), string)

    def test_square_display(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        square = Square(1)
        square.display()
        sys.stdout = sys.__stdout__
        display = "#\n"
        self.assertEqual(captured_output.getvalue(), display)

    def test_square_display1(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        square = Square(2, 1)
        square.display()
        sys.stdout = sys.__stdout__
        display = " ##\n ##\n"
        self.assertEqual(captured_output.getvalue(), display)

    def test_square_display2(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        square = Square(2, 1, 1)
        square.display()
        sys.stdout = sys.__stdout__
        display = "\n ##\n ##\n"
        self.assertEqual(captured_output.getvalue(), display)

    def test_square_to_dictionary(self):
        square = Square(2, id = 1)
        dictionary = square.to_dictionary()
        expected_dict = {'x': 0, 'y': 0, 'id': 1, 'size': 2}
        self.assertEqual(dictionary, expected_dict)

    def test_square_update(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        square.update(89)
        self.assertEqual(square.id, 89)

    def test_square_update1(self):
        square = Square(1, 2, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        square.update(89, 3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 3)

    def test_square_update2(self):
        square = Square(2, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 2)
        square.update(89, 4, 6)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 6)

    def test_square_update3(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        square.update(89, 5, 6, 3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 3)

    def test_square_update_kwarg(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        kwargs = {"id": 72}
        square.update(**kwargs)
        self.assertEqual(square.id, 72)

    def test_square_update_kwarg1(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        kwargs = {"id": 73, "size": 8}
        square.update(**kwargs)
        self.assertEqual(square.id, 73)
        self.assertEqual(square.size, 8)

    def test_square_update_kwarg2(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        kwargs = {"id": 22, "size": 5}
        square.update(**kwargs)
        self.assertEqual(square.id, 22)
        self.assertEqual(square.size, 5)

    def test_square_update_kwarg3(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        kwargs = {"id": 22, "size": 5, "x": 5}
        square.update(**kwargs)
        self.assertEqual(square.id, 22)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 5)

    def test_square_update_kwarg4(self):
        square = Square(1, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        kwargs = {"id": 22, "size": 5, "x": 5, "y": 10}
        square.update(**kwargs)
        self.assertEqual(square.id, 22)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 10)

    def test_square_create(self):
        dictionary = {"id" : 89}
        sqr = Square.create(**dictionary)
        self.assertEqual(sqr.id, 89)

    def test_square_create1(self):
        dictionary = {"id" : 89, "size": 42}
        sqr = Square.create(**dictionary)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 42)

    def test_square_create2(self):
        dictionary = {"id" : 89, "size": 13}
        sqr = Square.create(**dictionary)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 13)

    def test_square_create3(self):
        dictionary = {"id" : 89, "size": 13, "x": 3}
        sqr = Square.create(**dictionary)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 13)
        self.assertEqual(sqr.x, 3)

    def test_square_create4(self):
        dictionary = {"id" : 89, "size": 13, "x": 3, "y": 4}
        sqr = Square.create(**dictionary)
        self.assertEqual(sqr.id, 89)
        self.assertEqual(sqr.size, 13)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 4)

    def test_square_save_to_file(self):
        Square.save_to_file(None)
        filename = "Square.json"
        json_repr = None
        expected_repr = "[]"
        with open(filename, "r") as f:
            json_repr = f.read()
        self.assertEqual(json_repr, expected_repr)

    def test_square_save_to_file2(self):
        Square.save_to_file([])
        filename = "Square.json"
        json_repr = None
        expected_repr = "[]"
        with open(filename, "r") as f:
            json_repr = f.read()
        self.assertEqual(json_repr, expected_repr)

    def test_square_save_to_file3(self):
        Square.save_to_file([Square(1)])
        filename = "Square.json"
        json_repr = None
        with open(filename, "r") as f:
            json_repr = f.read()
        sqr = Square(5)
        dictionary = json.loads(json_repr)[0]
        sqr.update(**dictionary)
        self.assertEqual(sqr.size, 1)

    def test_square_load_from_file(self):
        if not os.path.exists('Square.json'):
            list_obj = Square.load_from_file()
            self.assertIsInstance(list_obj, list)
            self.assertEqual(list_obj, [])

    def test_square_load_from_file2(self):
        if os.path.exists('Square.json'):
            list_obj = Square.load_from_file()
            self.assertIsInstance(list_obj, list)
            for obj in list_obj:
                self.assertIsInstance
