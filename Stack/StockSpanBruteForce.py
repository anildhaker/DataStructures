# The stock span problem is a financial problem where we have a series of
#  n daily price quotes for a stock and we need to calculate span of stock’s
# price for all n days. 
# The span Si of the stock’s price on a given day i is defined as the maximum
# number of consecutive days just before the given day, for which the price of
# the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as
# {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days
# are {1, 1, 1, 2, 1, 4, 6}


# Fills list S[] with span values
def calculateSpan(price, n, S):

# Span value of first day is always 1
  S[0] = 1

# Calculate span value of remaining days by linearly
# checking previous days
  for i in range(1, n, 1):
    S[i] = 1 # Initialize span value

# Traverse left while the next element on left is
# smaller than price[i]
    j = i – 1
    while (j>= 0) and (price[i] >= price[j]) :
      S[i] += 1
      j -= 1

# A utility function to print elements of array
def printArray(arr, n):

  for i in range(n):
  print(arr[i], end = ” “)

# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n

# Fill the span values in list S[]
calculateSpan(price, n, S)



# print the calculated span values
printArray(S, n)