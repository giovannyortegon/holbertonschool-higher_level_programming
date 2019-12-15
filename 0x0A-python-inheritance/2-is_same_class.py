#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ exactly an instance of the specified class
        Args:
            obj: an instance
            a_class: type of class
        Return:
            True or fase acordding if it is an instance

    """
    if a_class is not object:
        return isinstance(obj, a_class)
