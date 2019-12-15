#!/usr/bin/python3
class Square:
    """ Square class
    Calculate the square area
    """
    def __init__(self, size=0):
        """ __init__ method
        """
        self.size = size

    @property
    def size(self):
        """ recive size value from __init__ and sett in setter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size stter method
        Args:
            size: integer number
        Raises:
            TypeError: if size is not integer
            ValueError: is size is less than 0
        """
        if type(value) is str:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Calculate area
        Args:
            size: only type integer
        Return:
            result of the area
        """
        return self.size ** 2

    def my_print(self):
        """ my_print print '#' according size value
        Args:
            size: only type integer
        """
        if self.size == 0:
            print()
        for i in range(0, self.size):
            print("{}".format('#' * self.size))
