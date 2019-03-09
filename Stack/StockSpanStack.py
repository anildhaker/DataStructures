# The stock span problem is a financial problem where we have a series of
#  n daily price quotes for a stock and we need to calculate span of stock’s
# price for all n days. 
# The span Si of the stock’s price on a given day i is defined as the maximum
# number of consecutive days just before the given day, for which the price of
# the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as
# {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days
# are {1, 1, 1, 2, 1, 4, 6}


def calculateSpan(price, S):
  n = len(price)

  stack = []

  stack.append(0)  #pushed index of first element

  S[0] = 1  #span value of first element will always be 1

  for i in range(1, n):
    while (len(stack) > 0 and price[stack[-1]] <= price[i]):
      stack.pop() 
  
    S[i] = i + 1 if len(stack) <= 0 else (i - stack[-1]) 
  
        # Push this element to stack 
    stack.append(i) 