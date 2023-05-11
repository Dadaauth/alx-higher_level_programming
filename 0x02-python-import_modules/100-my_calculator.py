#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    argC = len(argv)
    if (argC != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operations = ['+', '-', '*', '/']
    operator = argv[2]
    for i in operations:
        if (i == operator):
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    add_t = add(a, b)
    sub_t = sub(a, b)
    mul_t = mul(a, b)
    div_t = div(a, b)
    if operator == '+':
        print("{0} {1} {2} = {3}".format(a, operator, b, add_t))
    elif operator == '-':
        print(f"{a} {operator} {b} = {sub(a, b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {mul(a, b)}")
    elif operator == '/':
        print(f"{a} {operator} {b} = {div(a, b)}")
