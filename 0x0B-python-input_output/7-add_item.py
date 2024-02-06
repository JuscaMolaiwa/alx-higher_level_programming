#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_arguments_to_list(args):
    try:
        # Load existing items from the file if it exists
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        items = []

    # Add the new arguments to the list
    items.extend(args)

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    # Exclude the script name (argv[0]) from the arguments
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)

