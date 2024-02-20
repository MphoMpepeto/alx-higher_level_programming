#!/usr/bin/python3
"""Defines a file-writing function that returns the number of chars in text."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to be written to the file.
    Returns:
        The number of characters in the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
