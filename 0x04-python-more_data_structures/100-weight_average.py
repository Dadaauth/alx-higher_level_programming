#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    home = 0
    school = 0
    for i, j in my_list:
        home += i * j
    for i, j in my_list:
        school += j
    return float(home / school)


# my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
# result = weight_average(my_list)
# print("Average: {:0.2f}".format(result))
