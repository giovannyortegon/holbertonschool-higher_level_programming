#!/usr/bin/python3
for alpha in range(122, 96, -1):
    print(
        "{}".format(chr(alpha))
        if alpha % 2 != 1 else chr(alpha - 32), end="")
