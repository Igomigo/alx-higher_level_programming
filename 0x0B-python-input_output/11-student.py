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

    def to_json(self, attrs=None):
        """returns a dict representation of a Student instance"""
        if isinstance(attrs, list) and \
                all(isinstance(i, str) for i in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all the attributes of the Student instance
        with the json dict key-value pairs
        """
        for k, v in json.items():
            setattr(self, k, v)
