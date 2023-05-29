#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("{:d}".format(int(value)))
        return False


# print(safe_print_integer(2342))
