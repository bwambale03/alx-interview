def pascal_triangle(n):
    # Return an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize triangle as an empty list.
    triangle = []

    # For each row from 0 to n-1:
    for i in range(n):
        # Create a new row with 1 at the beginning.
        row = [1]

        # For each element from 1 to row_index:
        for j in range(1, i):
            # Calculate value as the sum of the two elements above.
            value = triangle[i-1][j-1] + triangle[i-1][j]
            # Append value to the row.
            row.append(value)

        # Append 1 at the end of the row.
        if i > 0:
            row.append(1)

        # Add the row to the triangle.
        triangle.append(row)

    # Return triangle.
    return triangle

# Example usage
n = 5
pascals_triangle = pascal_triangle(n)
for row in pascals_triangle:
    print(row)
