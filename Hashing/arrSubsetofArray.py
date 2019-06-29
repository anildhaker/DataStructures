# Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset
# of arr1[] or not. Both the arrays are not in sorted order. It may be assumed that
# elements in both array are distinct.


def isSubSet(arr1, arr2):
  h = set()
   
  if len(arr1) > len(arr2):
    for i in range(len(arr1)):
      h.add(arr1[i])

    for j in range(len(arr2)):
      if j not in h:
        return False
      else:
        return True
  else:
    for i in range(len(arr2)):
      h.add(arr2[i])

    for j in range(len(arr1)):
      if j not in h:
        return False
      else:
        return True
