class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None

  def Push(self,data):
    newNode = self.Node(data)
    newNode.next = self.top
    self.top = newNode

  def Pop(self):
    if self.isEmpty():
      return - 1
      
    temp = self.top
    self.top = self.top.next
    popped = temp.data
    return popped
  
  def isEmpty(self):
    if self.top == None:
      return True
    return False