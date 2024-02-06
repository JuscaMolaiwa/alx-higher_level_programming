ii#!/usr/bin/python3
"""A script to add command-line arguments to a list and save them to a JSON file."""
import sys
from my_json_functions import save_to_json_file, load_from_json_file

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")

