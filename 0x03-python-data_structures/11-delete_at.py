#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(0, len(my_list)):
        if i == idx:
            del my_list[idx: idx + 1]
    return my_list
