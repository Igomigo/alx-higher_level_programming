#!/usr/bin/python3
"""
module that contains the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the base class.
    attributes:
        __width: private instance attribute
        __height: private instance attribute
        __x: PIA
        __y: PIA
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for the width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height attr"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """To set the x attr"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """To get the y attr"""
        return self.__y

    @y.setter
    def y(self, value):
        """To set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
