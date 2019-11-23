# move the last element to the front

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

  def printlList(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next

  def lastToFront(self):
    prev = None
    curr = self.head
    
    while curr.next:
      prev = curr
      curr = curr.next
      
    prev.next = None
    curr.next = self.head
    self.head = curr 
  
llist = LinkedList() 
llist.push(700) 
llist.push(758) 
llist.push(30) 
llist.push(70)
llist.push(10)
llist.push(38)
llist.push(17)

print("Before swapping --")
llist.printlList()

print("After Swaping --")
llist.lastToFront()
llist.printlList()