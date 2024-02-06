#!/usr/bin/python3
"""
================================
Module with method is_same_class
================================
"""


def is_same_class(obj, a_class):
    """this method will return True if an object is an instance of a class"""

    return type(obj) is a_class
