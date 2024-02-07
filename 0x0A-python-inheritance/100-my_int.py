#!/usr/bin/python3
"""Module that Defines a MyInt Class that inherits from int."""


class MyInt(int):
    """Inverts int operators equals to == and not eqauls to !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
