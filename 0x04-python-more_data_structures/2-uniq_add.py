#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = []
    add = 0
    for j in my_list:
        if j not in uniq_list:
            add += j
            uniq_list.append(j)
    return add

# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))
