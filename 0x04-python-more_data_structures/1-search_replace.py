#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(0, len(my_list)):
        if search == my_list[i]:
            new_list.insert(i, replace)
        else:
            new_list.insert(i, my_list[i])
    return new_list
