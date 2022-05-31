#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if str[i] == ' ':
            print(" ", end='')
        elif ord(str[i]) > 64 and ord(str[i]) < 91:
            continue
        else:
            print("{:c}".format(ord(str[i]) - 32), end='')
