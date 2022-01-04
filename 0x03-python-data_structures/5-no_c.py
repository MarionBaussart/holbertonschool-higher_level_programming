#!/usr/bin/python3
"""
function that removes all characters c and C from a string
"""


def no_c(my_string):
    my_string = my_string.translate({ord(char): None for char in 'cC'})
    return (my_string)
