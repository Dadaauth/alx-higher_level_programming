#!/usr/bin/python3
"""
Another version of isinstanceof
"""


def is_same_class(obj, a_class):
    """
    checks if an object is exactly an instance of
    a specified class
    """
    if a_class == object:
        newInstance = a_class
    else:
        newInstance = a_class(obj)
    return obj == newInstance


a = [3, 4, 5]
print(is_same_class(a, object))
