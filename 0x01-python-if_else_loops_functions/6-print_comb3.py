#!/usr/bin/python3
for d1 in range(0, 10):
    for d2 in range(0, 10):
        if d1 < d2:
            if d1 < 8:
                print("{}{}".format(d1, d2), end=", ")
            else:
                print("{}{}".format(d1, d2), end="")
print()
