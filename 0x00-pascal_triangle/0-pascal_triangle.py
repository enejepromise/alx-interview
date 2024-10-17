#!/usr/bin/python3
"""
Contains a pascal triangle implementation
"""


def pascal_triangle(n):
    """
    Creates a list of lists, representing Pascal's Triangle

    Args:
        n (int): Height of triangle

    Returns:
        list[list[int]]: Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
