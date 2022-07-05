#!/usr/bin/python3
"""Module BaseGeometry"""


class BaseGeometry():
    """empty class"""

    def area(self):
        """ area exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator docstring raises
            exceptions based on the value passed """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
