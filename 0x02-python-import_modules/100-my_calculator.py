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
    match operator:
        case '+':
            print(f"{a} {operator} {b} = {add(a, b)}")
        case '-':
            print(f"{a} {operator} {b} = {sub(a, b)}")
        case '*':
            print(f"{a} {operator} {b} = {mul(a, b)}")
        case '/':
            print(f"{a} {operator} {b} = {div(a, b)}")
