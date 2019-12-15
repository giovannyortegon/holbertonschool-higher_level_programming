#!/usr/bin/python3
def uppercase(str):
    for ls in str:
        lr = ord(ls) - 32
        print(
            "{}".format(chr(lr))
            if ord(ls) >= 97 and ord(ls) <= 122 else ls, end="")
    print()
