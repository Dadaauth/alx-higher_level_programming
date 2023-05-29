#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while i < x:
            print(my_list[i], end='')
            i += 1
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count

# print(safe_print_list([1, 2, 3, 4, 5, 6], 2))
