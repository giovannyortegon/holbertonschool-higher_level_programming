#!/usr/bin/python3
""" Import Rectangle Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """ Show Args """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Update Args """
        try:
            Args = ('id', 'size', 'x', 'y')
            n_args = len(args)
            if n_args == 1:
                self.id = args[0]
            for i, arg in enumerate(args):
                setattr(self, Args[i], arg)
        except IndexError:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Convert args to dict """
        to_dict = {}
        args = ['id', 'x', 'size', 'y']
        for key in args:
            value = getattr(self, key)
            to_dict.update({key: value})

        return to_dict
