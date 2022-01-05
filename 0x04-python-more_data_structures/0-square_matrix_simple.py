#!/usr/bin/python3
"""
function that computes the square value of all integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    square_matrix = matrix.copy
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = matrix[row][column] ** 2
    return (square_matrix)
