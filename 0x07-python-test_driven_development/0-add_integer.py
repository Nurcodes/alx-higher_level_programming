#!/usr/bin/python3


""" This function takes two args: a and b
    converts them to ints from floats if they are
    are computes the sum.
    Return Value will be a + b
    raise exceptions for certain edge cases detailed"""


def add_integer(a, b=98):
    '''Returns an int: the sum of a and b
    Args: a (int): first arg
          b (int): second arg'''

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
