# Reversal algorithm for right rotation of an array

def reverseArray(arr, start, end):

  while (start < end):
    arr[start], arr[end] = arr[end], arr[start]
    start = start + 1
    end = end - 1
    
  
def rightRotation(arr,d,n): # n -Length of arr , d = number of rotations. 
  reverseArray(arr, 0, n - 1)
  reverseArray(arr, 0, d - 1)
  reverseArray(arr, d, n - 1)
  

def printArray(arr):
  for i in range(len(arr)):
    print(arr[i], end=' ')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Before Rotation -->")
printArray(arr)
rightRotation(arr, 3, 10)
print()
print("After Rotation -->")
printArray(arr)

