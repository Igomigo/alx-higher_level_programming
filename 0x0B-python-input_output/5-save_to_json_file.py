#!/usr/bin/python3
"""
A module that contains the function
def save_to_json_file(my_obj, filename)
"""

import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an object to a text file
    using a JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
