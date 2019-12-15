#!/usr/bin/python3
def append_write(filename="", text=""):
    """ Append a text
    Args:
        filename: any file
        text:   an string
    Return:
        characters written
    """
    with open(filename, 'a') as f:
        char = f.write(text)
    f.close()
    return char
