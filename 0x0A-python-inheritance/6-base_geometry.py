#!/usr/bin/python3
class BaseGeometry:
    """ BaseGeometry
    """
    def area(self):
        """ Raise:
            Exception: Error if it is called
        """
        raise Exception('area() is not implemented')
