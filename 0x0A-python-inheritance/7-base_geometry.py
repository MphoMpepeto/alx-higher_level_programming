#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Reps base geometry."""

    def area(self):
        """area not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a para as an integer.

        Args:
            name (str): The name.
            value (int): The para to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
