#!/usr/bin/python3
upper = False
for i in range(122, 96, -1):
    if upper:
        character = chr(i - 32)
        upper = False
    else:
        character = chr(i)
        upper = True
    print("{0}".format(character), end='')
