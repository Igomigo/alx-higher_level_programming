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
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
