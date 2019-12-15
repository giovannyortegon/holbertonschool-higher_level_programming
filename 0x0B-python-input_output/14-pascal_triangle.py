#!/usr/bin/python3

def pascal_triangle(n):
    _list=[]
    if n <= 0:
        return _list
    else:
        for i in range(n):
            print(_list)
            newlist=[]
            newlist.append(_list[0])
            for i in range(len(_list)-1):
                newlist.append(_list[i]+_list[i+1])
            newlist.append(_list[-1])
            _list=newlist
    return _list
