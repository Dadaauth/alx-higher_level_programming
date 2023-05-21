#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for key in a_dictionary:
        val = a_dictionary[key]
        if val == value:
            to_delete.append(key)
    for string in to_delete:
        del a_dictionary[string]
    return a_dictionary
