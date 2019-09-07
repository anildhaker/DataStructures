# finiding minimum element in sorted and rotated array.

# Input: {5, 6, 1, 2, 3, 4}
# Output: 1

# Method 1 - Linear search
def minElement(arr):
  minVal = float('inf')
  for i in range(len(arr)):
    if arr[i] < minVal:
      minVal = arr[i]

  return minVal

arr = [5, 6, 1, 2, 3, 4]
print(minElement(arr))

# Method 2 - O(LogN)
# Smallest value will have it's previous value greater than itself.

def minEleBinary(arr):
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
  
  # decide where to shift
  
  if arr[high] > arr[mid]:
    high = mid - 1
    return minEleBinary(arr)
  else:
    low = mid + 1
    return minEleBinary(arr)

arr = [5, 6, 1, 2, 3, 4]
print(minEleBinary(arr))