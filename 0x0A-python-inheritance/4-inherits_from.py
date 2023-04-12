#!/usr/bin/python3
"""
A module that contains a function that checks
if a class is a subclass of a parent class directly
"""


def inherits_from(obj, a_class):
    """the function that checks"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
