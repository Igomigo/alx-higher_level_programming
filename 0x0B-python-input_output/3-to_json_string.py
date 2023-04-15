#!/usr/bin/python3
import json

"""
A module that contains a function def to_json_string()
"""


def to_json_string(my_obj):
    """
    The function that returns the JSON representation
    of an object(string)
    """
    return json.dumps(my_obj)
