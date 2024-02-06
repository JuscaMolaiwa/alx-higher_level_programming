#!/usr/bin/python3
# from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
