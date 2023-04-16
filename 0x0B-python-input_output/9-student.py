#!/usr/bin/python3
"""
module that contains a class "Student"
"""


class Student:
    """
    class that defines a student by:
    first_name, last_name, and age.
    public metthod:
         to_json(self): retieves a dictionary representation
         of a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """initializes the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict representation of a Student instance"""
        return self.__dict__
