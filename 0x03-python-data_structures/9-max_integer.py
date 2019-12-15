#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    else:
        _max = 0
        for a in range(0, len(my_list)):
            if my_list[a] > _max:
                _max = my_list[a]
        return _max
