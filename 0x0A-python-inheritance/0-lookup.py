#!/usr/bin/python3
"""Defines a function that returns the list of available attributes and methods of an object."""

def lookup(obj):
    """Returns a list of an object's available attributes."""
    return (dir(obj))
