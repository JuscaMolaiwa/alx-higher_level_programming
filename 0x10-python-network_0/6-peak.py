def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.
    
    Args:
    - list_of_integers: A list of integers
    
    Returns:
    - A peak integer from the list
    """
    if not list_of_integers:
        return None
    
    left, right = 0, len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return list_of_integers[left]
