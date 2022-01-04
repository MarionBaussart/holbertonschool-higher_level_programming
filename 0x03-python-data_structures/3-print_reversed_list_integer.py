#!/usr/bin/python3
"""
function that replaces an element of a list at a specific position
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for integer in my_list:
        print("{}".format(integer))
