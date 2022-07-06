#!/usr/bin/python3
"""
    module for Pascal's triangle
"""


def pascal_triangle(n):
    """
        function for Pascal's triangle
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        layer = []
        for j in range(i + 1):
            if j == 0 or j == i:
                layer.append(1)
            else:
                layer.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(layer)
    return triangle
