#!/usr/bin/python3
"""
A module with the BaseGeometry class
"""


class BaseGeometry:
    """ contains a public attribute area()"""
    def __init__(self):
        pass

    def area(self):
        """public attribute raises an Exception"""
        raise Exception("area() is not implemented")
