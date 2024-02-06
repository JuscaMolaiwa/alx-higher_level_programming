#!/usr/bin/python3
""" utility function to retrieve a list of available attributes and methods of an object."""


def lookup(obj):
    """Returns A list containing the names of attributes and methods.."""
    return (dir(obj)
