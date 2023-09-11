#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    work = False
    for i in sys.argv:
        if work:
            sum += int(i)
        work = True
print(sum)
