#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_m = []
    for row in matrix:
        square_m.append([x ** 2 for x in row])
    return square_m
