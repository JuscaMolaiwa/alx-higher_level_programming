#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Class that defines a square with a private size attribute.
    """
    def __init__(self, size):
        """Instantiates a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
