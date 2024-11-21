#!/usr/bin/python3
"""function that rotate a 2D matrix in a place"""


def rotate_2d_matrix(matrix):
    """Rotate n x n 2D matrix, rotate it 90 degrees clockwise
    
    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)
    for c in range(n):
        for r in range(c, n):
            matrix[c][r],matrix[r][c] = matrix[r][c],matrix[c][r]
    for row in matrix:
        row.reverse()
