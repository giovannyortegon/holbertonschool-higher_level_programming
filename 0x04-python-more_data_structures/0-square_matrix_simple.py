#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def pow(x):
        return x ** 2

    return list(list(map(pow, matrix[i])) for i in range(0, len(matrix)))
