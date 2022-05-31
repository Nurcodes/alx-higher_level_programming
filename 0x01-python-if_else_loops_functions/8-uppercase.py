#!/usr/bin/python3
str = "Teest One 98"
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print("{:c}".format(ord(str[i]) - 32), end='')
        else:
            print("{}".format(str[i]), end='')
uppercase(str)
print('\n')
