#!/usr/bin/python3 env
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
def generate_pascals_triangle(n):

    triangle = []

    for i in range(n):
        row = [1]


        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]

            row.append(value)


        if value > 0:
            row.append(1)

        triangle.append(row)
    return triangle

# example usage
n=5
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)
