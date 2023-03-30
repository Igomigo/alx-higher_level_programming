#!/usr/bin/python3
""" A class that defines a square """


class Square:
    """ Square with private instance size and validation """
    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
