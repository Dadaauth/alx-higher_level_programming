#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if str(i) + str(j) < str(89):
            print("{0}{1}".format(i, j), end=', ')
        else:
            print("{0}{1}".format(i, j))
