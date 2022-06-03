#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        separator = ""
        for j in range(len(matrix[i])):
            print(separator, "{:d}".format(matrix[i][j]), sep="", end="")
            separator = " "
        print()
