#!/usr/bin/python3
""" This module creates a function which reads a text file """


def read_file(filename=""):
    """ reads a file with with statement """

    with open(filename, 'r', encoding='utf-8') as f:
        """ using open and with statements """
        print(f.read(), end='')
