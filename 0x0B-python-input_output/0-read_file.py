#!/usr/bin/python3
"""
A module that contains the read_file function
"""


def read_file(filename=""):
    """
    A function that reads a text file and prints
    it to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
