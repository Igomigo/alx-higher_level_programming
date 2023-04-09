#!/usr/bin/python3

"""
A module that contains a function (text_indentation(text) that prints a text
with two new lines after each of the characters '.', '?', and ':'.
"""


def text_indentation(text):
    """
    The function that prints a text with two new lines.
    after the punctuation marks above.

    Arg:
       text: the text argument.
    returns:
       modified text with two new lines each after the punctuation marks above.
    """

    checker = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if checker == 0:
            if i == ' ':
                continue
            else:
                checker = 1

        if checker == 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                checker = 0
            else:
                print(i, end="")
