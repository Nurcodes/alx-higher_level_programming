#!/usr/bin/python3
""" Import base """


from .base import Base


class Rectangle(Base):
    """ rectangle class inherits from base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ call the super() """

        super(Rectangle, self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @staticmethod
    def validatedim(name, value):
        """ Static method """
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be > 0')

    @staticmethod
    def validatepos(name, value):
        """ Static method """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value < 0:
            raise ValueError(name + ' must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
