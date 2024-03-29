#!/usr/bin/python3
"""Defines a string-to-JSON representation of the object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of the string object."""
    return json.dumps(my_obj)
