#!/usr/bin/python3
"""Module that Defines an inherited MyList Class."""


class MyList(list):
    """Custom list subclass with added functionality."""

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        print(sorted(self))
