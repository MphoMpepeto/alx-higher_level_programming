#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    print(f'{number} is negative')
if number > 0:
    print(f'{number} is positive')
if number == 0:
    print(f'{number} is zero')
