#!/usr/bin/python3
"""
This module defines the MyList class, which is a subclass of the built-in list class.
MyList provides additional functionality,
including a method to print its elements sorted.
"""

class MyList(list):
    """Custom list subclass with added functionality."""
    pass
    
    def print_sorted(self):
        """Prints the elements of the list in sorted order."""

        print(sorted(list(self)))

