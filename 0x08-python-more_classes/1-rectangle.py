#!/usr/bin/python3
""" A class that defines a rectangle """


class Rectangle:
    """ A rectangle with atributes and methods """
    def __init__(self, width=0, height=0):
        """ initializes the rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ A getter to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ A setter with validation to modify the value of the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter to retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter with validation to set the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
