# Reverse a stack without using extra space in O(n)

# Reverse a Stack without using recursion and extra space. Even the functional Stack is not allowed.

# Examples:

# Input : 1->2->3->4
# Output : 4->3->2->1

# Input :  6->5->4
# Output : 4->5->6


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
  
  def push(self, data):
    if self.head is None:
      self.head = Node(data)

    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  def pop(self):
    if self.head is None:
      return None
    else:
      popped = self.head.data
      self.head = self.head.next
      return popped
    
  def reverse(self):
    prev = None
    cur = self.head

    while (cur):
      nex = cur.next
      cur.next = prev
      prev = cur
      cur = nex
    self.head = prev

  def print_Stack(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next


stack = Stack() 
stack.push(20) 
stack.push(4) 
stack.push(15) 
stack.push(85)

stack.print_Stack()
print()
stack.reverse()
stack.print_Stack()

