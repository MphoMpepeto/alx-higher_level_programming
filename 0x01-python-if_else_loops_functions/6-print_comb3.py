#!/usr/bin/python3
for n in range (10):
    for i in range(n + 1, 10):
        print('{:01d}{:01d}'.format(n, i), end=', ' if n < 9 else "\n")
