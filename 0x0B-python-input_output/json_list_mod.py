#!/usr/bin/python3

from 7-add_item import load_from_json_file, \
        save_to_json_file

new_file = load_from_json_file("add_item.json")

new_file.pop(-1)

save_to_json_file(new_file, "add_item.json")
