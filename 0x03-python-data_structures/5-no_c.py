#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    for idx in new_str:
        if idx is 'c' or idx is 'C':
            new_str.remove(idx)
    new_str = ''.join(new_str)
    return new_str
