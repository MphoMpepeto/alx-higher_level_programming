#!/usr/bin/python3
"""Defines a JSON file-creating function."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename) as x:
        return json.load(x)
