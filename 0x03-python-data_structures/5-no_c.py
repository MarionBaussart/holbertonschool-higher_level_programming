#!/usr/bin/python3
"""
function that removes all characters c and C from a string
"""


def no_c(my_string):
    characters = "cC"
    for char in range(len(characters)):
        my_string = my_string.replace(characters[char],"")
    return (my_string)
