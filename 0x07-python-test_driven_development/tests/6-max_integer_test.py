#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    
    def set_up(self):
        self.list_num = [1, 2, 3, 4]

    def test(self):
        self.assertTrue(max_integer(list_num))


if __name__ == '__main__':
    unisttest.main()
