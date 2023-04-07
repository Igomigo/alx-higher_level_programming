#!/usr/bin/python3

"""
A module with a function, (print_square()), that prints a square with
the character #.
"""


def print_square(size):
    """
    The function that prints a square

    arg:
       size: size length of the square.
    return:
       the square of size with the character #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
