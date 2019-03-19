def isEmpty(stack):
  return len(stack) == 0

def Pop(stack):
  if isEmpty(stack):
    print("Stack underflow")
    exit(1)
  else:
    popped = stack.pop()
    return popped

def createStack():
  stack = []
  return stack

def push(stack, item):
  stack.append(item)
    

def sort_stack(stack):
  if not isEmpty(stack):
    temp = Pop(stack)
    sort_stack(stack)
    sorted_insert(stack, temp)

def top(stack):
  if not isEmpty(stack):
    return stack[-1]
  return False

def sorted_insert(stack, element):
  if isEmpty(stack) or element > top(stack):
    push(stack, element)
  else:
    temp = Pop(stack)
    sorted_insert(stack, element)
    push(stack, temp)

def print_stack(stack):
  for i in range(len(stack) - 1, -1, -1):
    print(stack[i], end="\n")

stack = createStack() 
push( stack, 10 ) 
push( stack, 30 ) 
push( stack, 2 ) 
push(stack, 15)



print_stack(stack)
print("\n")
sort_stack(stack)
print_stack(stack)


    




