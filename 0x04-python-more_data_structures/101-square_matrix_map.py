#!/bin/usr/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda num: num ** 2, row)),
                    matrix.copy()))
