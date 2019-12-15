#!/usr/bin/python3:
class Node:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data


    @data.setter
    def data(self, value):
        if type(value) == str:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next(self):
        return self.__next

    @data.setter
    def next(self, value):
        if value != None or Node()
            self.__next = value
        else:
            raise TypeError('next_node must be a Node object')
        
        


class SinglyLinkedList:
    def __init__(self)
