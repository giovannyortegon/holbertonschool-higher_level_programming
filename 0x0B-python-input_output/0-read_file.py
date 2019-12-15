#!/usr/bin/python3
def read_file(filename=""):
    """ open a file and read it
    Args:
        filename: any file.
    """
    with open(filename, "r") as f:
        line = f.read()
        print(line, end="")
    f.close()
