# A sorted array is rotated at some unknown point, find the minimum element in it.
# Following solution assumes that all elements are distinct.

# Aim is to find it in O(LogN) time complexity. 

def findLowest(arr):
  n = len(arr)
  low = 0
  high = len(arr) - 1
  
  if high < low:
    return arr[0]

  if high == low:
    return arr[low]

  mid = int((low + high) / 2)
  
  if mid < high and arr[mid + 1] < arr[mid]:
    return arr[mid + 1]
  
  if mid > low and arr[mid] < arr[mid - 1]:
    return arr[mid]

  # If none of above conditions satisfied then we will change low and high
  if arr[high] > arr[mid]:
    high = mid-1
    return findLowest(arr)
  else:
    low = mid+1
    return findLowest(arr)
  
  
arr = [4, 5, 1, 2, 3]
print(findLowest(arr))
  