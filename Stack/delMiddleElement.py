class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []
  
  def push(self, item):
    return self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]
  
  def size(self):
    return len(self.items)

  #Delete Middle node -- in case of Even number of elements - delete first one

def delMiddle(stack, n, curr):
  if stack.is_empty() or curr == n:
    return

  x = stack.peek()
  stack.pop()

  delMiddle(stack, n, curr + 1)

  if curr != n // 2:
    stack.push(x)


st = Stack() 
   
# push elements into the stack 
st.push('1') 
st.push('2') 
st.push('3') 
st.push('4') 
st.push('5') 
st.push('6') 
st.push('7') 
   
delMiddle(st, st.size(), 0)

#print Stack after deletion

while not st.is_empty():
  p = st.peek()
  st.pop()
  print(str(p) + " ", end='')
  

  


  
  

  
