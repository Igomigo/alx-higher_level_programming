#!/usr/bin/python3
"""
A module that contains a class
"""


class MyList(list):
    """
    A class that inherits from a list.

    methods:
       print_sorted(): A public instance method that sorts a list
       in ascending order.

    returns:
       A sorted list.
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
