# Delete middle element of a stack

# Given a stack with push(), pop(), empty() operations, delete middle of it without using any additional data structure.

# Input  : Stack[] = [1, 2, 3, 4, 5]
# Output : Stack[] = [1, 2, 4, 5]

# Input  : Stack[] = [1, 2, 3, 4, 5, 6]
# Output : Stack[] = [1, 2, 4, 5, 6]

class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def isEmpty(self):
    return self.items == []
    
  def pop(self):
    return self.items.pop()

  def top(self):
    return self.items(len(self.items) - 1)
    
  def size(self):
    return len(self.items)


def deleteMid(st, n, cur):
  if (st.isEmpty() or cur == n) : 
        return
  x = st.peek() 
  st.pop()
  
  deleteMid(st, n, cur + 1)

  if (cur != int(n/2)) : 
        st.push(x)
        
st = Stack() 
   
# push elements into the stack 
st.push('1') 
st.push('2') 
st.push('3') 
st.push('4') 
st.push('5') 
st.push('6') 
st.push('7')

deleteMid(st, st.size(), 0)

while (st.isEmpty() == False) : 
    p = st.peek() 
    st.pop() 
    print (str(p) + " ", end="") 

  

  
  
      
    
