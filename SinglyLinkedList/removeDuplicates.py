# Remove the Duplicate nodes in a sorted Linked list.

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

  def deleteNode(self, key):
    
    # if head node itself is node to be deleted
    temp = self.head
    
    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        temp = None
        return
        
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next

    if temp == None: # key not present in the list 
      return  
    prev.next = temp.next
    temp = None

  
  def removeDuplicates(self):
    temp = self.head
    
    if temp is None:
      return
      
    while temp.next is not None:
      if temp.data == temp.next.data:
        new = temp.next.next
        temp.next = None
        temp.next = new
        
      else:
        temp = temp.next
      
    return self.head 


llist = LinkedList() 
llist.push(7) 
llist.push(7) 
llist.push(3) 
llist.push(3)
llist.push(1)

print("Before removal of duplicates--")
llist.printlList()

print("After removal of duplicates --")
llist.removeDuplicates()
llist.printlList()