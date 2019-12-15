#!/usr/bin/python3
""" import Base class"""
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        list_obj = []
        if json_string:
            list_obj = json.loads(json_string)
        return list_obj

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        objs = []
        if list_objs:
            for obj in list_objs:
                objs.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(
                    cls.to_json_string(objs))
            f.close()
        else:
            with open(cls.__name__ + ".json", "w+") as f:
                f.write(
                    cls.to_json_string(objs))
                f.close()

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 2)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ load form file """
        filename = cls.__name__ + ".json"
        ins_obj = []
        try:
            with open(filename, "r") as f:
                objs = cls.from_json_string(f.read())
                for obj in objs:
                    ins_obj.append(cls.create(**obj))
            return ins_obj
        except Exception:
            return ins_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file csv """
        with open(cls.__name__ + ".csv", "w+") as f:
            obj_write = csv.writer(f, delimiter=',')
            if list_objs:
                obj_write.writerow(list(list_objs[0].to_dictionary().keys()))
                for i, ins_obj in enumerate(list_objs):
                    obj_write.writerow(list(ins_obj.to_dictionary().values()))
            else:
                obj_write.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        """ load from file csv """
        rec_args = ('id', 'width', 'height', 'x', 'y')
        sq_args = ('id', 'size', 'x', 'y')
        dict_obj = {}
        inst_obj = []
        if cls.__name__ == "Square":
            args = sq_args
        else:
            args = rec_args
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                obj_read = csv.DictReader(f)
                for row in obj_read:
                    for arg in args:
                        dict_obj.update({arg: int(row[arg])})
                    inst_obj.append(cls.create(**dict_obj))
            return inst_obj
        except Exception:
            return inst_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw """
