#!/usr/bin/python3
"""Defines a dictionary description ."""


def class_to_json(obj):
    """Returns the dictionary description with a simple data structure."""
    return obj.__dict__
