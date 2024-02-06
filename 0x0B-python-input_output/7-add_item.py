ii#!/usr/bin/python3
"""A script to add command-line arguments to a list and save them to a JSON file."""

import sys
from my_json_functions import save_to_json_file, load_from_json_file

if __name__ == "__main__":
    # Importing the functions for saving and loading from JSON files

    # Attempting to load existing items from the file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []  # If the file doesn't exist, start with an empty list

    # Adding the command-line arguments to the list
    items.extend(sys.argv[1:])

    # Saving the updated list to the file
    save_to_json_file(items, "add_item.json")

