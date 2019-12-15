#!/usr/bin/python3
class MyList(list):
    """ Recide a list
        Args:
            list(list): is a list empty
        Attributes:
            pop: return an elemento for position and after delete it
            append: add at the end
            insert: insert an element in the indicated position
            index: serach in a position indicated
            extend: fusion two lists
            remove: delete a element first time

    """
    def __getitem__(self, key):
        """ recive arguments of attributes of a list
            Args:
                key(int): is an element

        """
        return list.__getitem__(self, key + 1)

    def print_sorted(self):
        """ print a sorted list
        """
        print(sorted(self, key=int))
