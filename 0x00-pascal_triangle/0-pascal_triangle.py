#!/usr/bin/python3
"""
Module that contains a function that returns a list of lists
of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integer
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]  # Start the row with 1

        for j in range(1, i):

            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle
