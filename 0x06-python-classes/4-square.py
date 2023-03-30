#!/usr/bin/python3
""" Class that defines a square """


class Square:
    """
    A class square with private instance size, a getter,
    a setter and public instance method area
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter method that returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method that sets the size of the attribute"""
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """public instance method that returns the current square area"""
        return self.__size ** 2
