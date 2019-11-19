# remove duplicate Nodes - in an unsorted linked list

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

# We will use Hashing here     
  def removeDuplicates(self):
    s = set()
    curr = self.head
    prev = None
    
    while curr:
      if curr.data not in s:
        s.add(curr.data)
        prev = curr
        curr = curr.next
      else:
        prev.next = curr.next
        curr = None
        curr = prev.next
    return self.head 


llist = LinkedList() 
llist.push(7) 
llist.push(7) 
llist.push(3) 
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(1)

print("Before removal of duplicates--")
llist.printlList()

print("after Removal --")
llist.removeDuplicates()
llist.printlList()