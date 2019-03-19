# Sort a stack using a temporary stack

# Given a stack of integers, sort it in ascending order using another temporary stack.

# Examples:

# Input : [34, 3, 31, 98, 92, 23]
# Output : [3, 23, 31, 34, 92, 98]

# Input : [3, 5, 1, 4, 2, 8]
# Output : [1, 2, 3, 4, 5, 8]


def createStack(): 
    stack = [] 
    return stack 

def isEmpty( stack ): 
    return len(stack) == 0
  
def push( stack, item ): 
    stack.append( item ) 
   
def top( stack ): 
    p = len(stack) 
    return stack[p-1] 
  
def pop( stack ):  
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
  
    return stack.pop() 
  
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print()
    
def sortStack(stack):
  tempStack = createStack()

  while (not isEmpty(stack)):
    temp = top(stack)
    pop(stack)

    while (not isEmpty(tempStack) and top(tempStack) > temp):
      push(stack, top(tempStack))
      pop(tempStack)

    push(tempStack, temp)
  
  return tempStack


stack = createStack() 
push( stack, 34) 
push( stack, 3) 
push( stack, 31) 
push( stack, 98)  
push( stack, 92) 
push( stack, 23)

print("Sorted numbers are: ") 
sortedst = sortStack ( stack ) 
prints(sortedst) 

  