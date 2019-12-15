#!/usr/bin/python3
class Square:
    """ Square class
    Calculate the square area
    """
    def __init__(self, size=0):
        """ __init__ method
        Args:
            size: integer number
        Raises:
            TypeError: if size is not integer
            ValueError: is size is less than 0
        """
        if type(size) is str:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """ Calculate area
        Args:
            size: only type integer
        Return:
            result of the area
        """
        return self.__size ** 2
