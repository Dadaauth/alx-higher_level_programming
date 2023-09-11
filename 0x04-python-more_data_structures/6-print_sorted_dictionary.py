#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    listed = sorted(a_dictionary)
    new_dict = dict()
    for i in listed:
        print("{0}: {1}".format(i, a_dictionary[i]))


# a_dictionary = {'language': "C", 'Number': 89, 'track': "Low le"
#                "vel", 'ids': [1, 2, 3]}
# print_sorted_dictionary(a_dictionary)
