#!/usr/bin/python3
"""
A module that defines a function that
adds attributes to objects.
"""


def add_attribute(obj, att, value):
    """Function that adds a new attribute to an object if possible.
    Args:
        obj: The object to add an attribute to.
        att: The name of the attribute to add to obj.
        value: The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
        "can't add new attribute"
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
