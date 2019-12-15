#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ if the object is an instance of a class that inherited
        Args:
            obj: an instance
            a_class: type of class
        Return:
            True or fase acordding if it is an instance

    """
    if obj.__class__ is not a_class:
        return isinstance(obj, a_class)
