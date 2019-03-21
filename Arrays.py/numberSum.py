# sum from 1 to n



def sum_numbers(n):
  total = 0 
  for i in range(1, n + 1):
    total = total + i
  
  return total
print("enter a number : ")
x = int(input())
print(sum_numbers(x))
print()



