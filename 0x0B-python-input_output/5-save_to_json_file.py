#!/usr/bin/python3
"""Defines a JSON text file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as x:
        json.dump(my_obj, x)
