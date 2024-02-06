#!/usr/bin/python3
"""Defines a function to insert text after each line containing a given string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within each line of the file.
        new_string (str): The string to insert after each line containing the search string.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
