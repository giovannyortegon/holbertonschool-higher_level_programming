#!/usr/bin/python3
""" This function ``matrix_divided``
    Divide the elements of a maxtrix by any integer number,
    recive two arguments, a matrix and one dividend and
    return a new list  with results.
"""


def matrix_divided(matrix, div):
    """ ``matrix_divided`` Function
        recide two arguments a matrix and dividend
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) is str:
        raise TypeError('div must be a number')
    elif type(matrix) is not list or matrix is None:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for i in range(0, len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        elif len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
    return [[round(j / div, 2) for j in i] for i in matrix]
