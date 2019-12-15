#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """ convert an object in json string
    """
    return json.dumps(my_obj, sort_key=True)
