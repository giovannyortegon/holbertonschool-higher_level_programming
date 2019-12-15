#!/usr/bin/python3
class MyInt(int):
    """ Entry a integer
    """
    def __eq__(self, value):
        """ never is equal
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """ nagating the return value
        """
        return super().__eq__(value)
