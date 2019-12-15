#!/usr/bin/python3
""" import Base class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ Rectangle Area """
        return self.__width * self.__height

    def display(self):
        """ Show Rectangle """
        print("\n" * self.__y, end="")
        for w in range(self.__height):
            print(" " * self.__x, end="")
            for h in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ __str__ """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update Args """
        try:
            Args = ('id', 'width', 'height', 'x', 'y')
            n_args = len(args)
            if n_args == 1:
                self.id = args[0]
            for i, arg in enumerate(args):
                setattr(self, Args[i], arg)
        except IndexError:
            pass
        # **kwarg
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Convert args to dict """
        args = ['x', 'y', 'id', 'height', 'width']
        to_dict = {}
        for key in args:
            value = getattr(self, key)
            to_dict.update({key: value})

        return to_dict
