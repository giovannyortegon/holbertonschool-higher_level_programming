#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Write a text
    Args:
        filename: any file
        text:   an string
    Return:
        characters written
    """
    with open(filename, 'w') as f:
        char = f.write(text)
    f.close()
    return char
