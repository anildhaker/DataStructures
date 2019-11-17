# 3 case - 1. beginning 2. End 3. Insert after an element 

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_Node = Node(new_data)

    new_Node.next = self.head
    self.head = new_Node

  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print("Given prev Node must be present in Linked List")
      return
      
    new_Node = Node(new_data)

    new_Node.next = prev_node.next
    prev_node.next = new_Node
    

  def addInEnd(self, new_data):
    new_Node = Node(new_data)
    
    if self.head == None:
      self.head = new_Node

    temp = self.head
    while (temp.next):
      temp = temp.next
      
    temp.next = new_Node