#!/usr/bin/python3
"""
Contains the class MyInt that inherits from the int class
"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, second):
        return int(self) != second

    def __ne__(self, second):
        return int(self) == second
