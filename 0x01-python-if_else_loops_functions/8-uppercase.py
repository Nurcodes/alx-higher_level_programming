#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            i = ord(str[i]) - 32
    print("{:s}".format(str))
    print()
