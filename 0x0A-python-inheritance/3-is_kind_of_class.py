#!/usr/bin/python3
"""
====================================
Module with function is_kind_of_class
====================================
"""


def is_kind_of_class(obj, a_class):
    """Check if the given object is an instance of the specified class or a subclass.
    returns  True if the object is an instance of the class or a subclass, False otherwise. """

    return isinstance(obj, a_class)
