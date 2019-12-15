#!/usr/bin/python3
import json


def from_json_string(my_str):
    """ Data structure represented by a JSON
    Args:
        my_str: date
    Return:
        Data structure
    """
    return json.loads(my_str)
