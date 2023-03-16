#!/usr/bin/python3

def search_replace(my_list, search, replace):
    element = my_list.index(search)
    my_list[element] = replace
    return my_list
