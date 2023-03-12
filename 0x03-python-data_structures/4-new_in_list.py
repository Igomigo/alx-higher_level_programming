#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        list = my_list[:]
        my_list[idx] = element
        return(list)
    else:
        return(my_list)
