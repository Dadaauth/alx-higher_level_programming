"""
A matrix division module
This module handles all the logics for matrix division
It is the best module you can get in the market
It has only one function
but that one function is capable of handling a lot of logic
"""


def matrix_divided(matrix, div):
    """
    small but mighty
    a function used to divide matrixes by a particular number.
    div is that number, div must be an integer or a float
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for a in matrix:
        if type(a) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for b in a:
            if type(b) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        size = len(matrix[0])
        if len(a) is not size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row = []
    for a in matrix:
        for b in a:
            b = round(b / div, 2)
            row.append(b)
        new_matrix.append(row)
        row = []
    return new_matrix


m = [
        [12, 35, 45, 55, 64],
        [198, 108, 980, 345, 65]
]
