#!/usr/bin/python3
""" ``say_my_name``
    print first name and last name
    recive: fisrt name(str), last name(str)
    if it is different to str print Error 
"""


def say_my_name(first_name, last_name=""):
    """ ``say_my_name``:
        recide two dates string type
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
