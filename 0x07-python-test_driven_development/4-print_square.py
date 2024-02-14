#!/usr/bin/python3

"""Module that prints a square with pound symbol."""

def print_square(size):
    """Method for printing a square with # character.
    Args:
        size: The int size of the square/ length of each side.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is a negative integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
