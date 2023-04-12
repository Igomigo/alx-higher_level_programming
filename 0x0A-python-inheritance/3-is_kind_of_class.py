#!/usr/bin/python3
"""
A module that contains a function that checks if an object is
an instance of a specified class
"""


def is_kind_of_class(obj, a_class):
    """ The function that does the check"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
