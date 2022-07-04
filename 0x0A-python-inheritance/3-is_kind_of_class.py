#!/usr/bin/python3
""" if instance of or if the object is inherited super class"""

def is_kind_of_class(obj, a_class):
    """ use isinstance with this one """

    if isinstance(obj, a_class):
        return True
    return False
