#!/usr/bin/python3
"""Defines a text file line insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as x:
        for line in x:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(text)
