#!/usr/bin/python3
"""Mylist class inherits from list
    def print sorted that prints list but sorted"""


class MyList(list):
    """Inherits from list class

    Args:
        list (obect): type list
    """

    def print_sorted(self):
        """This one was to easy for your own good!!!"""
        print(sorted(self))
