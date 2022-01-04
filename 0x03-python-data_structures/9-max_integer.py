#!/usr/bin/python3
"""
function that finds the biggest integer of a list
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        integer_max = 0
        for integer in my_list:
            if integer > integer_max:
                integer_max = integer
        return (integer_max)
