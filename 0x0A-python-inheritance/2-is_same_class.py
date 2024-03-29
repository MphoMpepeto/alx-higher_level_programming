#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check for  class.
        a_class (type): The class to match the type of object to.
    Returns:
        If the object is exactly an instance of a_class - True.
        If not - False.
    """
    if type(obj) == a_class:
        return True
    return False
