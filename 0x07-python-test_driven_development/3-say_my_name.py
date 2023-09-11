#!/usr/bin/python3

"""
Say my name module
it has only one function
it prints `My name is <first name> <last name>`
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function
    ::
        a function that says a person's name passed to it
        first_name and last_name must be strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    message = "My name is {0} {1}"
    print(message.format(first_name, last_name))
