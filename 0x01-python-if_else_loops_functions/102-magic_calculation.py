#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if a == 0:
        return a
    elif b == 2:
        return len(b)
    else:
        return c

dis.dis(magic_calculation)
