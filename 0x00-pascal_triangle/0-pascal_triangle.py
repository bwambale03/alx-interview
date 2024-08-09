#!/usr/bin/python3

#Pascal's Triangle

'''
Initialize triangle as an empty list.
For each row from 0 to n-1:
    Create a new row with 1 at the beginning.
    For each element from 1 to row_index:
        Calculate value as the sum of the two elements above.
        Append value to the row.
    Append 1 at the end of the row.
    Add the row to the triangle.
Return triangle.

'''


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row as a list of lists.

    :param n: The number of rows to generate.
    :return: A list of lists representing Pascal's triangle.
    """
    pascal_tri = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            pascal_tri.append([1])
        else:
            cur_row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    cur_row.append(1)
                else:
                    cur_row.append(pascal_tri[i - 1][j - 1] +
                                   pascal_tri[i - 1][j])

            pascal_tri.append(cur_row)

    return (pascal_tri)
    