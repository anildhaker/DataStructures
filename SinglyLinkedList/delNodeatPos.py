# DELETE NODE AT A GIVEN POSITION

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def printlList(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next 

  def push(self, new_data): 
    new_node = Node(new_data) 
    new_node.next = self.head 
    self.head = new_node
      
  def deleteNode(self, position):
    # list is empty 
    if self.head == None:
      return
      
    temp = self.head
    
    if position == 0:
      self.head = temp.next
      temp = None
      return
      
    for i in range(position - 1):
      temp = temp.next
      if temp is None:
        break
      
    if temp is None:
      return
      
    if temp.next is None:
       return
       
    # we have iterated till Pos - 1 ... so now prev of the node to be deleted is stored
    # in temp. ... and node to be deleted is temp.next.
    
    # storing the pointer of node to be deleted.
    nxt = temp.next.next
    
    temp.next = None
    
    temp.next = nxt 


llist = LinkedList() 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 
llist.push(8)


print("before deletion --")
llist.printlList()

llist.deleteNode(2)
print("After deletion--")
llist.printlList()