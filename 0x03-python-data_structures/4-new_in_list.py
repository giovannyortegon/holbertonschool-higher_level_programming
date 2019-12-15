#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        new_list = []
        for index in range(0, len(my_list)):
            if index is idx:
                new_list.insert(index, element)
            else:
                new_list.insert(index, my_list[index])
        return new_list
