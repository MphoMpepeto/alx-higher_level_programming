#!/usr/bin/python3
for letters in range(ord('z'), ord('a') - 1, -1):
    curr_letter = chr(letters)
    if (letters - ord('z')) % 2 == 0:
        print('{}'.format(chr(letters).lower()), end='')
    else:
        print('{}'.format(chr(letters).upper()), end='')
