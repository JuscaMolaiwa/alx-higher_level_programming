#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

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

        If attrs is a list of strings, only attributes included in the list
        will be represented.

        Args:
            attrs (list): (Optional) A list of attribute names to represent.
                If provided, only attributes in this list are included in
                the dictionary.
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student with the provided dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values
                to replace in the Student instance.
        """
        for k, v in json.items():
            setattr(self, k, v)
