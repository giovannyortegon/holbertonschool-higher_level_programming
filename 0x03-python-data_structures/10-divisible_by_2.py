#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in range(0, len(my_list)):
        op = my_list[i] % 2
        if op == 0:
            result.append(True)
        else:
            result.append(False)
    return result
