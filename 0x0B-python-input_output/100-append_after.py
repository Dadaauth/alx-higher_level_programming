#!/usr/bin/python3
"""
Searches and updates a file at specific sections
"""


def check_same(haystack, needle):
    """
    checks for the same
    """
    for y in range(len(needle)):
        if y == len(haystack):
            return False
        if haystack[y] != needle[y]:
            return False
    return True


def find_str(system, component):
    """
    the parent same checker
    """
    idx = 0
    c_p = ''
    for char in system:
        if char == component[0]:
            c_p = system[idx:]
            if check_same(c_p, component):
                return True
        idx += 1
    return False


def append_after(filename="", search_string="", new_string=""):
    """
    a function to append after
    """
    line_number = 1
    line_list = []
    with open(filename, 'r') as f:
        for line in f:
            if find_str(line, search_string):
                line_list.append(line_number)
            line_number += 1
    with open(filename, 'a') as f:
        current_line = 1
        for line_num in line_list:
            while current_line < line_num:
                f.readline()
                current_line += 1
            f.write(new_string)


# append_after("README.md", 'ALXSE', "Authority Place")
# test_str = "Yoho pp pythod wpd ooood Pythonx  x"
# search = "Pythonx  "

# if find_str(test_str, search):
#    print('The string was found!')
# else:
#    print('No such metadata')
