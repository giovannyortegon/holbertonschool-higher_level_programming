#!/usr/bin/python3
class Square:
    """ Square class
    Calculate the square area
    Args:
        size(int): recive a integer number
        position(tuple): recive a tuole
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ recive size value from __init__ and sett in setter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter method
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

    @property
    def position(self):
        """ recive position tuple from __init__ and sett in setter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter method
        Args:
            value: integer number
        Raises:
            TypeError: if size is not integer
        """
        if len(value) == 1 or type(value) != tuple or \
                type(value[0]) == str or type(value[1]) == str:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ calculate area
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
            position: value tuple
        """
        if self.size == 0 or self.position[1] > 0:
            print()
        for i in range(0, self.size):
            print("{}{}".format(' ' * self.position[0], '#' * self.size))
