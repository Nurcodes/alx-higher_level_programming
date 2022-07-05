#!/usr/bin/python3
""" This module appends new text add end of file """


def append_write(filename="", text=""):
    """ function which appends text to filename """

    with open(filename, 'a', encoding='utf-8') as f:
        """ appends text to file object """
        return f.write(text)
