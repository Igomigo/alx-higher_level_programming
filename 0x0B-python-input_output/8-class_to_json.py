#!/usr/bin/python3
"""
Contains the def class_to_json(obj) function
"""


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    dict_obj = obj.__dict__
    return dict_obj
