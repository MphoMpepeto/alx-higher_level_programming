#!/usr/bin/python3
"""Add two integers together."""


def add_integer(a, b=98):
    """A function that adds two integers.

    Args:
        a: 1st integer.
        b: 2nd integer, assigned value = 98.

    Raises:
        TypeError: if a and b are not integers.

    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
