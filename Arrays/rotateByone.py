# Program to cyclically rotate an array by one
# Given an array, cyclically rotate the array clockwise by one.

# Examples:

# Input:  arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}


# Following are steps.
# 1) Store last element in a variable say x.
# 2) Shift all elements one position ahead.
# 3) Replace first element of array with x.


def rotationByOne(arr):
  n = len(arr)
  x = arr[-1]
  for i in range(n-1,0,-1):
    arr[i] = arr[i-1]
  arr[0] = x
  return arr

arr = [1, 2, 3, 4, 5]

print(rotationByOne(arr))
