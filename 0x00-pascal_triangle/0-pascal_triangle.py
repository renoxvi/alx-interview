#!/usr/bin/python3
"""
Print Pascal's Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        last_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(last_row)):
            new_row.append(last_row[i - 1] + last_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle