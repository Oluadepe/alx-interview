#!/usr/bin/python3
"""
Pascal's Triangle function
"""


def pascal_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle

n = 5
for row in pascal_triangle(n):
    print(row)
