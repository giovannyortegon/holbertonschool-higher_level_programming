#!/usr/bin/python3
def number_of_lines(filename=""):
    """ Count number of lines of a file

    Args:
        filename:   Any file

    Return:
        number of lines

    """
    n_line = 0
    with open(filename, 'r') as f:
        for line in f:
            n_line += 1
    f.close()
    return n_line
