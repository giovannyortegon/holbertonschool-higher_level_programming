#!/usr/bin/python3
def remove_char_at(str, n):
    try:
        if n < 0:
            return str
        new = list(str)
        new.remove(new[n])
        new = ''.join(new)
        return new
    except IndexError:
        return str
