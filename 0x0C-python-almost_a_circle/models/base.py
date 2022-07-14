#!/usr/bin/python3
"""Base.py Module"""


class Base:
    """ Class Base with private class attribute,
    a class constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method for the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
