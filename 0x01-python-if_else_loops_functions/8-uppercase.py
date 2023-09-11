#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for character in str:
        ascii_decimal = ord(character)
        if islower(character):
            character = chr(ascii_decimal - 32)
        print("{0}".format(character), end='')
    print()


# uppercase("hello my Name IS Clement")
