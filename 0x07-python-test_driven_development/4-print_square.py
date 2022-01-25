#!/usr/bin/python3
"""
Module containing print_square function
"""


def print_square(size):
    """ function that prints a square with the character #
    Args:
        size: int, size of the square
    Return: no return.
    Raise:
        TypeError: size must be an integer
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
