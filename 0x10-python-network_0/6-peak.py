def find_peak(list_of_integers):
  """
  Function to find a peak in a list of unsorted integers.

  Args:
      list_of_integers: A list of integers

  Returns:
      A peak integer from the list (may not be the only one)
  """
  if list_of_integers is None or len(list_of_integers) == 0:
    return None

  if len(list_of_integers) == 1:
    return list_of_integers[0]

  start = 0
  end = len(list_of_integers) - 1

  # Use binary search to find a potential peak
  while start < end:
    mid = start + (end - start) // 2

    # Check if middle element is a peak (greater than both neighbors)
    if (mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]) and \
       (mid == len(list_of_integers) - 1 or list_of_integers[mid] > list_of_integers[mid + 1]):
      return list_of_integers[mid]

    # Move search based on neighbors
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
      end = mid - 1
    else:
      start = mid + 1

  # If loop exits without finding a peak in the middle, 
  # the first or last element might be the peak (edge cases)
  return list_of_integers[0] if list_of_integers[0] > list_of_integers[1] else list_of_integers[-1]

# Write complexity to a file
with open("6-peak.txt", "w") as f:
  f.write("0(log n)")
