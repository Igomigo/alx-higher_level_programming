#!/usr/bin/python3
"""
A module that contains a function that takes one argument
def from_json_string(my_str).
"""

import json


def from_json_string(my_str):
    """
    A function that returns an object(python data structure)
    represented by a JSON string.
    """
    return json.loads(my_str)
