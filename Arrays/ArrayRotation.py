#  Using Temporary array

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

def arrRotation(arr,d):
  temp = [None] * d
  for i in range(d):
    temp[i] = arr[i]
    
  # print(temp)
  # # Shift rest of the array
  for j in range(0, len(arr) - d):
    print('before--',arr)
    arr[j] = arr[j + d]
    print('after---',arr)
  print(arr[0: len(arr) - d] + temp)
  

arrRotation(arr,2)