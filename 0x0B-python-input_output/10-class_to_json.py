#!/usr/bin/python3
def class_to_json(obj):
    objs = {}
    for idx, value in sorted(obj.__dict__.items()):
        objs[idx] = value

    return objs
