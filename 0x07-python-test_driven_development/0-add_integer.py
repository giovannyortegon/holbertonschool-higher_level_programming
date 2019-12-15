#!/usr/bin/python3
""" ``add_integer`` function
    This function that add two number integers in otherwise (float)
    number are casted to integer or if any of these is str raises an
    Error: TypeError if is empty or is str
"""


def add_integer(a, b=98):
    """ Args: a(int) and b(int)
        Returns: sum of two numbers
    """
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)
    elif type(a) is str or a is None:
        raise TypeError('a must be an integer')
    elif type(b) is str or b is None:
        raise TypeError('b must be an integer')
    return a + b
