#!/usr/bin/python3
"""tough module"""


def inherits_from(obj, a_class):
    """"function"""

    return type(obj) != a_class and isinstance(obj, a_class)
