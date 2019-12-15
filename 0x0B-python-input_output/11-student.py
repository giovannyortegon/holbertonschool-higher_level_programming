#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        objs = {}
        for idx, value in sorted(self.__dict__.items()):
            objs[idx] = value

        return objs
