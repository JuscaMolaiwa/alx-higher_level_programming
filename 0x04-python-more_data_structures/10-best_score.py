#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        if a_dictionary:  # Check if the dictionary is not empty
            max_score = max(a_dictionary.values())
            for key, value in a_dictionary.items():
                if value == max_score:
                    return key
    return None
