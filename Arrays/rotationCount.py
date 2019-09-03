# Consideranarrayofdistinctnumberssorted in increasingorder.
# Thearrayhasbeenrotated(clockwise)knumberoftimes.Givensuchanarray,
# find the value of k.

# Method 1 - Naive Approach - Linear Search 
def numRatationCount(arr):

  minVal = arr[0]

  for i in range(len(arr)):
    if minVal > arr[i]:
      minVal = arr[i]
      index = i

  return index

arr = [4, 5, 1, 2, 3]
print(numRatationCount(arr))

# Method 2 - Binary Search
def rotCount(arr):
  low = 0
  high = len(arr) - 1
  
  if high < low:
    return 0
  
  if high == low:
    return low

  mid = int((high + low) / 2)
  
  if mid < high and arr[mid + 1] < arr[mid]:
    return (mid + 1)
  
  if mid > low and arr[mid] < arr[mid - 1]:
    return mid

  # decide whether to move left or right
  
  if arr[high] > arr[mid]:
    high = mid -1 
    return rotCount(arr)

  else:
    low = mid + 1
    return rotCount(arr)


