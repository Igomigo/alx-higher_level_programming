#!/usr/bin/python3
"""
A module that contains the function
def load_from_json_file(filename).
"""


import json


def load_from_json_file(filename):
    """
    A function that creates an object from a
    "JSON file".
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        json.loads(data)
