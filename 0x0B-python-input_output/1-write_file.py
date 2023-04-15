#!/usr/bin/python3
"""
A module that contains the write_file function
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file and
    returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
