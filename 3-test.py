#!/usr/bin/python3
r = __import__("3-rectangle").Rectangle

my_rect = r(2, 4)
print("Area: {} - Perimeter: {}".format(my_rect.area(), my_rect.perimeter()))

print("--")

my_rect.width = 32
my_rect.height = 32
print("Area: {} - Perimeter: {}".format(my_rect.area(), my_rect.perimeter()))
print(str(my_rect))
print(repr(my_rect))
