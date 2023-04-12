#!/usr/bin/python3
"""
A module that contains the BaseGeometry class
"""


class BaseGeometry:
    """Class with two public instance methods:
            - area(self): that returns an Exception.
            - integer_validator(self, name, value): that validates
             value.
    """
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
