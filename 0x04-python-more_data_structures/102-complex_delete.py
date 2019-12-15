#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    f = 0
    new_list = []
    for k, v in a_dictionary.items():
        if value == v:
            new_list.append(k)
    for i in new_list:
        del a_dictionary[i]
    return a_dictionary
