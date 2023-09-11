#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_int = my_list[0]
    for i in range(0, len(my_list)):
        if max_int < my_list[i]:
            max_int = my_list[i]
    return max_int
# test_list = [97, 1, 2, 3, -97, 12, -13]
# print(test_list)
# print(max_integer(test_list))
