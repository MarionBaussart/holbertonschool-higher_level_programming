#!/usr/bin/python3
"""
function that computes the square value of all integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    square_matrix = []
    for number in matrix:
        square_matrix += [list(map(lambda x: x ** 2, number))]
    return (square_matrix)
