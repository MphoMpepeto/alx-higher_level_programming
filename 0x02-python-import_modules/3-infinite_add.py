#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    sum_arg = 0
    for n in range(1, len(argv)):
        sum_arg += int(argv[n])
    print('{}'.format(sum_arg))
