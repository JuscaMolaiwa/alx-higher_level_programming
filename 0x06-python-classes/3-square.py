#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Class that defines a square with a private size attribute."""
    def __init__(self, size=0):
        """Instantiates a square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = 0  # Default size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2
