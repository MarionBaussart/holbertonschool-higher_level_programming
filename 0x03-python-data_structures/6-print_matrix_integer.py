#!/usr/bin/python3
"""
function that prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print("{:d}".format(matrix[row][column]), end=" ")
        print()
