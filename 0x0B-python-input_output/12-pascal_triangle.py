#!/usr/bin/python3
"""This is a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tris.append(tmp)
    return tris
