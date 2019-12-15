#!/usr/bin/python3
for char in range(97, 123):
    if chr(char) == 'e' or chr(char) == 'q':
        continue
    else:
        print('{}'.format(chr(char)), end="")
