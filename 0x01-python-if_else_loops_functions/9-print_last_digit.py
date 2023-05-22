#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    elif number < 0:
        last_digit = number % -10
        last_digit *= -1
    print(last_digit, end='')
    return last_digit


# print_last_digit(98)
# print_last_digit(0)
# print_last_digit(-99391302)
# r = print_last_digit(-1024)
# print(r)
