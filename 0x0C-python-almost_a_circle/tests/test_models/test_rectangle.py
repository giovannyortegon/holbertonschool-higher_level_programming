#!/usr/bin/python3
""" import models """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import csv
import pep8


class Testpep8(unittest.TestCase):
    """ TestPEP8 """
    def test_pep8(self):
        """ test pep8 """
        pystyle = pep8.StyleGuide(quite=True)
        base_f = "models/base.py"
        base_test = "test/test_models/test_base.py"
        rectangle_f = "models/rectangle.py"
        rectangle_test = "test/test_models/test_rectangle.py"
        square_f = "models/square.py"
        square_test = "test/test_models/test_square.py"
        checker = style.check_files([base_f, base_test,
                                    rectangle_f, rectangle_test,
                                    square_f, square_test])
        self.assertEqual(checker.total_errors, 0,
                        "Found code style errors (and warning).")

class RectangleTest(unittest.Testcase):
    """ Rectangle Test """
    

    def setUp(self):
        """ setUp"""


if __name__ == "__main__":
    unittest.main()
