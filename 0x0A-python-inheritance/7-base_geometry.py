#!/usr/bin/python3
class BaseGeometry:
    """ BaseGeometry
    """
    def area(self):
        """ Raise:
            Exception: Error if it is called
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ valid value
            Raise:
                TypeError: if value is not integer
                ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
