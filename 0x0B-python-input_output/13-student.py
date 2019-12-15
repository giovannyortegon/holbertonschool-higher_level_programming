#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        objs = {}
        if type(attrs) is list:
            for idx, value in sorted(self.__dict__.items()):
                if idx in attrs:
                    objs[idx] = value
        else:
            for idx, value in sorted(self.__dict__.items()):
                objs[idx] = value

        return objs

    def reload_from_json(self, json):
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
