#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Class that defines a square with size and position attributes."""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiates a square with optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size  
        self.position = position

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

    @property
    def position(self):
        """Getter method to retrieve the current position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position with type and value validation.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
