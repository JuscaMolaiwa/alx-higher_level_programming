#!/usr/bin/python3
"""
This module provides a function to find a peak element in an unsorted list of integers.

A peak element is an element that is greater than both its neighbors.

The function `find_peak` takes a list of integers and return.
"""

def find_peak(list_of_integers):
    """
    Finds a peak (element greater than both neighbors) in an unsorted list of integers.
    Args:
      list_of_integers: A list of integers.
    Returns:
      The first peak element found in the list, or None if no peak exists.
    """
    if not list_of_integers:
        return None

    def peak_helper(nums, left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return peak_helper(nums, left, mid)
        else:
            return peak_helper(nums, mid + 1, right)

    return peak_helper(list_of_integers, 0, len(list_of_integers) - 1)
