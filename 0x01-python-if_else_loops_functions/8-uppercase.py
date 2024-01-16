#!/usr/bin/python3
def uppercase(str):
    string = ''
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            U_letter = chr(ord(letter) - ord('a') + ord('A'))
            string += '{}'.format(U_letter)
        else:
           string += '{}'.format(letter)
    print(string)

