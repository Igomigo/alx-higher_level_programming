#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        my_list = sorted(my_list)
        return my_list[-1]
