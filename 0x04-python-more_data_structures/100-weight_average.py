#!/usr/bin/python3
def weight_average(my_list=[]):
    return list(map(lambda i: list(map(lambda j: j**2, i)), my_list))
