class StackNode:

  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:

  # constructor for head node of Linked list
  def __init__(self):
    self.head = None
  
  def isEmpty(self):
    if self.head is None:
      return True
    return False
  
  def push(self, data):
    new_node = StackNode(data)
    new_node.next = self.head
    self.head = new_node

  def pop(self):
    if self.isEmpty():
      return
    temp = self.head
    self.head = self.head.next
    popped = temp.data
    return popped
  
  def peek(self):
    if self.isEmpty():
      return
    return self.head.data
  
stack = Stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
  
print(stack.pop())