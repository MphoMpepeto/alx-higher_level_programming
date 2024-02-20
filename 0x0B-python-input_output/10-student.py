#!/usr/bin/python3
"""Defines a class called Student."""


class Student:
    """Represents a student by name surname and age."""

    def __init__(self, first_name, last_name, age):
        """start a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attributes are a list of strings, represents only those attributes
        included in the list.

        Args:
            attr (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
