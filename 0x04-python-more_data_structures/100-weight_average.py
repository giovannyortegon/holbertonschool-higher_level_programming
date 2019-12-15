#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is []:
        return 0
    else:
        _sum = 0
        div = 0
        mul = 1
        for i in my_list:
            mul = 1
            f = 0
            for j in i:
                if f == 0:
                    mul = mul * j
                    f = f + 1
                else:
                    mul = mul * j
                    div = div + j
                    _sum = _sum + mul
        return _sum / div
