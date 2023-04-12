#!/usr/bin/python3
"""
Module containing a function(def is_same_class(obj, a_class)
that checks if an object is exactly an instance of the
specified class.
"""


def is_same_class(obj, a_class):
    """ The function that checks """
    if isinstance(obj, a_class):
        return True
    else:
        return False
