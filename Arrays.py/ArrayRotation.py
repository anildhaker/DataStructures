# Left Rotate Array By d elements

def leftRotate(arr, d, n):
  for i in range(d):
    leftRotatebyOne(arr, n)
    
def leftRotatebyOne(arr, n):
  temp = arr[0]
  for i in range(n - 1):
    arr[i] = arr[i + 1]
   
  arr[n-1] = temp

def printArray(arr):
  for i in range(len(arr)):
    print(arr[i], end=' ')
  print()
  
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7)

printArray(arr)