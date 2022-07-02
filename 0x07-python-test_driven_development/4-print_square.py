#!/usr/bin/python3
"""this module creates a square and
    prints it out with # symbol"""


def print_square(size):
    """Print a square with the size arg

    Args:
        Size (int) : size of square
    Raises:
        TypeError: size must be an ineger
        ValueError: if size is less than 0
        TypeError: if size is float and is less than 0 raise
    Return: a printed square with size"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
