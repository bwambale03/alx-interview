#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix in place."""

    if not isinstance(matrix, list) or len(matrix) == 0:
        return
    if not all(isinstance(row, list) for row in matrix):
        return
    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    # Actual rotation logic
    c, r = 0, rows - 1
    new_matrix = []

    for i in range(cols * rows):
        if i % rows == 0:
            new_matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        new_matrix[-1].append(matrix[r][c])
        r -= 1

    # Copy rotated matrix back to original
    matrix[:] = new_matrix
