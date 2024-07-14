#!/usr/bin/python3
"""
 Finds a peak (element greater than both neighbors) in an unsorted list of integers.

 Args:
  list_of_integers: A list of integers.

 Returns:
  The first peak element found in the list, or None if no peak exists.
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
