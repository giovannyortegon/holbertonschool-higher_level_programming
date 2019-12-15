#!/usr/bin/python3
def square_prueba(matrix=[]):
    return [[matrix[i][j] * 2 for j in range(len(matrix[i])) if j % 2 == 0 ] for i in
    range(len(matrix))if i % 2 == 0]
