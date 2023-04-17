#!/usr/bin/python3
"""
contains the function append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """
     A function that inserts a line of text to a file,
    after each line containing a specific string
    """
    temp_file = ""
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            temp_file += line
            if search_string in line:
                temp_file += new_string
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(temp_file)
