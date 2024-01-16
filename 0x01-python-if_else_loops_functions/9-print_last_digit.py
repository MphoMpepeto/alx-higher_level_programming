#!/usr/bin/python3
def print_last_digit(number):
    x = abs(number)
    last_digit = x % 10
    print(last_digit, end='')
    return last_digit
