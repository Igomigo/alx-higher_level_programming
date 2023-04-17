#!/usr/bin/python3
"""
A module that contains the pascal_triangle(n) function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the pascal's triangle of n.
    """
    if n <= 0:
        return []

    """initialize the list with the first row"""
    lst = [[1]]

    """generate the remaining row"""
    for i in range(1, n):
        row = []
        """append the first digit to row which is 1"""
        row.append(1)

        """create a prev_row variable to hold the previous
        row"""
        prev_row = lst[-1]

        """loop through the prev_row to generate
        the new row"""
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j+1])

        """append 1 at the end of the row list"""
        row.append(1)

        """append the new row to the list"""
        lst.append(row)
    """return the list"""
    return lst
