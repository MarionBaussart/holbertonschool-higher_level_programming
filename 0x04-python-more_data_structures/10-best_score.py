#!/usr/bin/python3
"""
function that returns a key with the biggest integer value
"""


def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    return (max(a_dictionary, key=a_dictionary.get))
