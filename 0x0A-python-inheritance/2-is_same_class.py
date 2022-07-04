#!/usr/bin/python3
"""Returns true or false based on isinstance(a, b)"""


def is_same_class(obj, a_class):
    """ either true or false """

    if type(obj) == a_class:
        return True
    return False
