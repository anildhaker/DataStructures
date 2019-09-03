# Given an array, only rotation operation is allowed on array.Wecanrotatethearray as
# many times as we want.Return the maximum possbile of
# summation of i*arr[i].


def maximumSum(arr):
  ArrSum = 0
  curVal = 0

  for i in range(len(arr)):
    ArrSum += arr[i]
    curVal += i*arr[i]
 
  maxVal = curVal
  n = len(arr)
  for j in range(1, len(arr)):
    curVal += ArrSum - n * arr[n - j]
    
    if curVal > maxVal:
      maxVal = curVal

  return maxVal

arr = [10,1, 2, 3, 4, 5, 6, 7, 8, 9]

print(maximumSum(arr))
