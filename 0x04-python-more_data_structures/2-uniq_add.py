#!/usr/bin/python3
"""
function that adds all unique integers in a list (only once for each integer)
"""


def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum = 0
    for number in uniq_list:
        sum += number
    return (sum)
