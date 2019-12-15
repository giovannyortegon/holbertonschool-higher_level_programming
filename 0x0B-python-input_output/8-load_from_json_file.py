#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ Read json from file
    Args:
        filename:   name file

    Return:
        obj: information
    """
    with open(filename, 'r') as f:
        obj = json.loads(f.read())
    f.close()
    return obj
