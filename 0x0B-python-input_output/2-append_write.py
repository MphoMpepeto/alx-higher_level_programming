#!/usr/bin/python3
"""Defines a file-appending a string to the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file and returns number of char.

    Args:
        filename (str): The name of the file to add to.
        text (str): The string to append to the file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
