#!/usr/bin/python3
def islower(c):
    ascii_decimal_value = ord(c)
    if 97 <= ascii_decimal_value < 123:
        return True
    else:
        False


# print("a is {}".format("lower" if islower("a") else "upper"))
# print("H is {}".format("lower" if islower("H") else "upper"))
# print("A is {}".format("lower" if islower("A") else "upper"))
# print("3 is {}".format("lower" if islower("3") else "upper"))
# print("g is {}".format("lower" if islower("g") else "upper"))
