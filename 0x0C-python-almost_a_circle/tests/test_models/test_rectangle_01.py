#!/usr/bin/python3
"""Module for test the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests for the instances width, height and id from rectangle class"""
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_objects()

    def test_id(self):
        """Test valid id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_ids(self):
        """Test valid ids"""
        r2 = Rectangle(32, 2)
        self.assertEqual(r2.id, 1)
        r3 = Rectangle(7, 2)
        self.assertEqual(r3.id, 2)
        r4 = Rectangle(32, 3, 0, 0, 77)
        self.assertEqual(r4.id, 77)

    def test_valid_parametrs(self):
        """Test with valid params"""
        r5 = Rectangle(3, 5, 2, 8, 108)
        self.assertEqual([r5.width, r5.height, r5.x, r5.y, r5.id],
                         [3, 5, 2, 8, 108])
        r6 = Rectangle(43, 23)
        self.assertEqual([r6.width, r6.height], [43, 23])

    def test_params_defaults(self):
        """Tests default values for x, y"""
        r7 = Rectangle(32, 12)
        self.assertEqual([r7.x, r7.y], [0, 0])

    def test_params_defaults_2(self):
        """Tests default params"""
        r8 = Rectangle(32, 32, 13)
        self.assertEqual([r8.width, r8.height, r8.x, r8.y, r8.id],
                         [32, 32, 13, 0, 1])

    def test_params_setters(self):
        """Check all setters"""
        r9 = Rectangle(32, 34)
        r9.width = 21
        self.assertEqual(r9.width, 21)
        r9.height = 87
        self.assertEqual(r9.height, 87)
        r9.x = 55
        self.assertEqual(r9.x, 55)
        r9.y = 444
        self.assertEqual(r9.y, 444)

    def test_params_exceptions_args(self):
        """Checks wrong number of arguments, zero"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_params_exceptions_args_one(self):
        """Checks wrong number of arguments, 1 args"""
        with self.assertRaises(TypeError):
            r = Rectangle(21)

    def test_params_exceptions_args_six(self):
        """Checks wrong number of arguments, six"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 23, 12, 234, 4)

    def test_args_value_zero(self):
        """Check valid value"""
        msg = " must be > 0"
        err = ValueError
        try:
            Rectangle(-10, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            Rectangle(10, -10)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)

        try:
            Rectangle(0, 10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            Rectangle(10, 0)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)

        msg = " must be >= 0"
        try:
            Rectangle(10, 10, -2)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            Rectangle(10, 10, 2, -3)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)
