#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ save json in file
    Args:
        my_obj: information
        filename: name of file

    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
    f.close()
