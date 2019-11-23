# pairwise swapping like following -
# Input : 1->2->3->4->5->6->NULL
# Output : 2->1->4->3->6->5->NULL

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
  
  def pairwiseSwap(self):
    temp = self.head
    
    if temp is None:
      return
      
    while (temp is not None and temp.next is not None):
      temp.data, temp.next.data = temp.next.data, temp.data
      # now look for next pair 
      temp = temp.next.next
      

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
llist.pairwiseSwap()
llist.printlList()

