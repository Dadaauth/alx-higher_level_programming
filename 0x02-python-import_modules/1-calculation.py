#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5
add = add(a, b)
sub = sub(a, b)
mul = mul(a, b)
div = div(a, b)

if __name__ == "__main__":
    print("{0} + {1} = {2}".format(a, b, add))
    print("{0} - {1} = {2}".format(a, b, sub))
    print("{0} * {1} = {2}".format(a, b, mul))
    print("{0} / {1} = {2}".format(a, b, div))
