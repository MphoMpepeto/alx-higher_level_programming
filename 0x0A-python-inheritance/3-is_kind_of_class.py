#!/usr/bin/python3
"""Defines a inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is an instance or inherited instance of a specified class - True.
        if not - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
