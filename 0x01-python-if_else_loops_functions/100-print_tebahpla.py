#!/usr/bin/python3
for letters in range(ord('z'), ord('a') - 1, -1):
    if (letters - ord('z')) % 4 < 2:
        print('{}'.format(chr(letters).lower()), end='')
    else:
        print('{}'.format(chr(letters).upper()), end='')
