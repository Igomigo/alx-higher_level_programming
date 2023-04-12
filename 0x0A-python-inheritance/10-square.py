#!/usr/bin/python3
"""
A  module that contains a subclass of the Rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ the square subclass that inherits from the
    class Rectagle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self.area(size, size)
        super().__Init__(size, size)
