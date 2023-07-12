#!/usr/bin/python3
"""
a module for creating pascal triangles
"""


def pascal_triangle(n):
    """
    a function that can create pascal triangles
    and return them as a list
    """
    full_list = []
    prev_list = []
    for a in range(1, n + 1):
        if len(prev_list) == 0:
            full_list.append([1])
            prev_list = [1]
            continue
        a_list = [1]
        for b in range(len(prev_list) - 1):
            a_list.append(prev_list[b] + prev_list[b + 1])
        a_list.append(1)
        prev_list = a_list
        full_list.append(a_list)
    return full_list

# import sys
# pascal = sys.argv[1]
# pascal = pascal_triangle(int(pascal))
# for i in pascal:
#     print(i)
