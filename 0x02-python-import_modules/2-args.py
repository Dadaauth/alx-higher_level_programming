#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argC = len(sys.argv) - 1
    if argC == 1:
        print("1 argument:")
    elif argC == 0:
        print("0 arguments.")
    else:
        print(f"{argC} arguments:")
    for i in range(1, argC + 1):
        print(f"{i}: {sys.argv[i]}")
