#!/usr/bin/python3
Rectangle = __import__("4-rectangle").Rectangle

my_rect = Rectangle(2, 4)
print(str(my_rect))
print("--")
print(my_rect)
print("--")
print(repr(my_rect))
print("--")
print(hex(id(my_rect)))
print("--")

# create a new instance based on representation
new_rect = eval(repr(my_rect))
print(str(new_rect))
print("--")
print(new_rect)
print("--")
print(repr(new_rect))
print("--")
print(hex(id(new_rect)))
print("--")

print(new_rect is my_rect)
print(type(new_rect) is type(my_rect))
