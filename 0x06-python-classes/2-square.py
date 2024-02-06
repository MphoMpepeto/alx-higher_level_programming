#!usr/bin/python3

"""This program writes a class square that defines a square with a private instance attribute which is size"""

class Square:
    """Defines a square qith size zero"""

    def __init__(self, size=0):
        """ 
        Args:
        size of square
        """

        if type(size) is int:
            
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
            self.__size = size
