#!/usr/bin/python3
"""
function that prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    for element in sorted(a_dictionary):
        print("{}: {}".format(element, a_dictionary.get(element)))
