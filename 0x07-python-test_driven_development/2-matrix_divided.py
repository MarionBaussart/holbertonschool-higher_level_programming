#!/usr/bin/python3
"""
Module containing matrix_divided function
"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix
    Args:
        matrix: list of lists of integers or floats we want to divide
        div: number (integer or float), the divider
    Return: new matrix divided by div
    Raise:
        TypeError: if elements of matrix or div aren't integers or floats /
            row of the matrix haven't the same size /
        ZeroDivisionError: div = 0
    """

    new_matrix = []
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_type)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elmt in row:
            if not isinstance(elmt, (int, float)):
                raise TypeError(msg_type)
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    


    for elmt in matrix:
        new_matrix += [list(map(lambda x: round(x / div, 2), elmt))]

    return new_matrix
