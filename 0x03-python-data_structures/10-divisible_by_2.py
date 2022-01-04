#!/usr/bin/python3
"""
function that finds all multiples of 2 in a list
Return a new list with True or False, depending on whether the integer at the
same position in the original list is a multiple of 2
"""


def divisible_by_2(my_list=[]):
    new_list = []
    for integer in my_list:
        if integer % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
