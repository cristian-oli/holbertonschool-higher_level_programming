#!/usr/bin/python3
"""Module for test the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestBaseClass(unittest.TestCase):
    """Tests method area from rectangle class"""
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_objects()

    def test_display(self):
        """Test display with valid arguments"""
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

    def test_display_valid(self):
        """Test display with valid arguments"""
        f = io.StringIO()
        s = ('#' * 32 + '\n') * 32
        r1 = Rectangle(32, 32)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('#' * 2 + '\n') * 52
        r2 = Rectangle(2, 52)
        with redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), s)
