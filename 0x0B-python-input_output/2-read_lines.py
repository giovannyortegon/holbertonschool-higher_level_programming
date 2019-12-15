#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ Read a number of lines of a file

    Args:
        filename(str):  Any file
        nb_lines(int):  integer number

    Return:
        number of lines

    """
    n_line = 0
    nl = 0
    with open(filename, 'r') as f:
        for line in f:
            n_line += 1
    f.close()
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines >= n_line:
            line = f.read()
            print(line, end="")
        else:
            for n, line in enumerate(f):
                if n == nb_lines:
                    break
                print(line, end="")
    f.close()
