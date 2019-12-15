#!/usr/bin/python3
def add_attribute(obj, name, value):
    """ New attribute to an object
        Add if belog at the dict
        Return:
            new set of attributes
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    return setattr(obj, name, value)
