#!/usr/bin/python3
"""Defines a Pascal Triangle."""


def pascal_triangle(n):
    """Represent Pascal Triangle of n that returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triA = triangles[-1]
        temp = [1]
        for i in range(len(triA) - 1):
            temp.append(triA[i] + triA[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
