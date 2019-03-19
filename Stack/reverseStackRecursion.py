def insertAtBottom(stack, item):
  if isEmpty(stack):
    push(stack, item)
  else:
    temp = pop(stack)
    insertAtBottom(stack, item)
    push(stack, temp)
    
def reverse(stack):
  if not isEmpty(stack):
    temp = pop(stack)
    reverse(stack)
    insertAtBottom(stack, temp)
    

def createStack():
  stack = []
  return stack

def push(stack, item):
  stack.append(item)


def pop(stack):
  if isEmpty(stack):
    print("Stack UnderFlow")
    exit(1)

  else:
    return stack.pop()
  
def isEmpty(stack):
  if len(stack) == 0:
    return True
  return False


def print_stack(stack):
  for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end="\n")
    


#Test the code:

stack = createStack() 
push( stack, str(4) ) 
push( stack, str(3) ) 
push( stack, str(2) ) 
push(stack, str(1))

print_stack(stack)



  
