# Given an array that is sorted and then rotated around an unknown point. 
# Find if the array has a pair with a given sum ‘x’. 
# It may be assumed that all elements in the array are distinct.

# Naive Approach
def isSumExist(arr, x):  # x is target sum here
  for i in range(len(arr)-1):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] == x:
        return True

# Finding the pivot and move lowest and highest value according to desired Sum.
# Method 2
def sumRotatedSorted(arr, x):
  n = len(arr)

  # Finding index of pivot element
  for i in range(len(arr)):
    if arr[i] > arr[i + 1]:
      break

  l = i + 1  # lowest value
  r = i  # highest value
  while(l!=r):
    if arr[l] + arr[r] == x:
      return True
    
    if arr[l] + arr[r] < x:
      l = (l + 1) % n
      
    else:
      r = (n + r - 1) % n
    
arr = [11, 15, 6, 8, 9, 10]

print(isSumExist(arr, 16))
print(sumRotatedSorted(arr, 16))


# Comments - To find the Pivot in O(logN) we can use Binary search.
# Hence solution can be further improvied. 


