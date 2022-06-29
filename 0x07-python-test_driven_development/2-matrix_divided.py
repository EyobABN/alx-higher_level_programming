#!/usr/bin/python3
"""
    module for dividing all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        function that divides a matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg)
    row_size = len(matrix[0])
    for row in matrix:
        if not type(row) is list:
            raise TypeError(msg)
        for cell in row:
            if not (type(cell) is int or type(cell) is float):
                raise TypeError(msg)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if div is None or (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
