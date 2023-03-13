#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    tuple = (length, first_char)
    if length == 0:
        result = (0, None)
        return result
    return tuple
