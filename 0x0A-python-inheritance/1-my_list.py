#!/usr/bin/python3
"""writes an inherited list class MyList from list."""

class MyList(list):
    """Implements prints an ordered built-in list class."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
