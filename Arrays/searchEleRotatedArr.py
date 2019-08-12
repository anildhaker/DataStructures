# An element in asortedarraycanbefound in O(logn)timeviabinarysearch.
# But suppose we rotate an ascending orders array at somepivotunknowntoyoubeforehand.
# So for instance, 1 2 3 4 5 mightbecome 3 4 5 1 2.Deviseawaytofindanelement
# in the rotated array in O(log n) time.


def findPivot(arr, low, high):
  if high < low:
    return - 1
  if high == low:
    return low
    
  mid = int((low + high) / 2)

  if mid < high and arr[mid] > arr[mid + 1]:
    return mid

  if mid > low and arr[mid] < arr[mid - 1]:
    return (mid - 1)

  if arr[low] >= arr[mid]:
    return findPivot(arr, low, mid - 1)
  else:
    return findPivot(arr, mid + 1, high)


def BinarySearch(arr, low, high, key):
  if high < low:
    return - 1
    
  mid = int((low + high) / 2)
  
  if key == arr[mid]:
    return mid
  
  if key > arr[mid]:
    return BinarySearch(arr, (mid + 1), high, key)
    
  else:
    return BinarySearch(arr, low, (mid - 1), key)



def pivotedBinarySearch(arr, n, key):
  pivot = findPivot(arr, 0, n - 1)
  
  if pivot == -1:
    return BinarySearch(arr, 0, n - 1, key)
    
  if arr[pivot] == key:
    return pivot
    
  if arr[0] <= key:
    return BinarySearch(arr, 0, pivot - 1, key)
    
  else:
    return BinarySearch(arr,pivot+1,n-1,key)

arr = [4, 5, 6, 1, 2, 3]

print(pivotedBinarySearch(arr,6,3))
