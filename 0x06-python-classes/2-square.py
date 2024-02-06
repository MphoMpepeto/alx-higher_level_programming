#!usr/bin/python3

"""This program writes a class square that defines a square with a private instance attribute which is size"""

class Square:
    """Defines a square qith size zero"""

    def __init__(self, size=0):

        """Define a new square with size 0.

        Args:
            (int) size: represents the new square size

        Raises:
            TypeError: If the given size is not an integer
            ValueError: If the given size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
