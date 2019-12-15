#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        my_list.sort(reverse=True)
        for idx in range(len(my_list)):
            print("{:d}".format(my_list[idx]))
