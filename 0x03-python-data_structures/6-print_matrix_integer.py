#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for row in range(0, len(matrix)):
            for colm in range(0, len(matrix[row])):
                print("{:d}".format(matrix[row][colm]), end='')
                if colm != (len(matrix[row]) - 1):
                    print(" ", end="")
            print()
