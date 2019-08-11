# Block swap algorithm for array rotation

# Initialize A = arr[0..d-1] and B = arr[d..n-1]
# 1) Do following until size of A is equal to size of B

#   a)  If A is shorter, divide B into Bl and Br such that Br is of same 
#        length as A. Swap A and Br to change ABlBr into BrBlA. Now A
#        is at its final place, so recur on pieces of B.  

#    b)  If A is longer, divide A into Al and Ar such that Al is of same 
#        length as B Swap Al and B to change AlArB into BArAl. Now B
#        is at its final place, so recur on pieces of A.

# 2)  Finally when A and B are of equal size, block swap them.


def leftRotate(arr, d, n):
  if d == 0 or d == n:
    return
    
  i = d
  j = n - d
  while (i != j):
    if (i < j):  # A is shorter
      swap(arr, d - i, d + j - i, i)
      j -= i
    else:
      swap(arr, d - i, d, j)
      i -= j

  swap(arr, d - i, d, i)



# /*This function swaps d elements starting at index fi 
#   with d elements starting at index si */

def swap(arr, fi, si, d):
  for i in range(d):
    temp = arr[fi + i]
    arr[fi + i] = arr[si + i]
    arr[si + i] = temp
    
  return arr
  
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


