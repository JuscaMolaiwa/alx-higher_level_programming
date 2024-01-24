#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Class that defines a square with a private size attribute.
    """
    def __init__(self, size=0):
        """Instantiates a square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Getter method to retrieve the current size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size with type and value validation.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
