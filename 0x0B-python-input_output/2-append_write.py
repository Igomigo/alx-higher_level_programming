#!/usr/bin/python3
"""
A module that contains the function append_write()
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the ennd of a text file
    and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
