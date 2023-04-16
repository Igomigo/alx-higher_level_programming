#!/usr/bin/python3
"""
A script that adds all
arguments to a python list, and save them to a file.
"""


from sys import argv

"""importing the 'save_to_json_file' function:"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""importing the 'load_from_json_file' function:"""
load_from_json_file \
        = __import__("6-load_from_json_file").load_from_json_file


file = "add_item.json"

try:
    pylist = load_from_json_file(file)
except FileNotFoundError:
    pylist = []

for i in argv[1:]:
    pylist.append(i)

save_to_json_file(pylist, file)
