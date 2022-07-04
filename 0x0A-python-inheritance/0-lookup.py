#!/usr/bin/python3

"""This function returns the list of
    available attributes and methods of an obj"""


def lookup(obj):
    """Takes an object as arg and returns dir(obj)

    Args:
        obj (object): class instance
    """
    return dir(obj)
