#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
try:
    print_square(9.5)
except Exception as b:
    print(b)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
try:
    print_square({'key': 89})
except Exception as j:
    print(j)
print("")
