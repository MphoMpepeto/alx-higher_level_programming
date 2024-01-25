#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dicti_copy = a_dictionary.copy()
    for x, y in dicti_copy.items():
        if value == y:
            a_dictionary.pop(x)
    return a_dictionary
