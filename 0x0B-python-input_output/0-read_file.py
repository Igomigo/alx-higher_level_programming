#!/usr/bin/python3

def read_file(filename=""):
    """
    A function that reads a text file and prints
    it to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data)
