# interSection of two sorted link lists.

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

  def add(self, new_data):
    temp = self.head

    if temp is None:
      self.head = Node(new_data)
      return
  
    while temp and temp.next is not None:
      temp = temp.next

    temp.next = Node(new_data)



def intersection(list1, list2):
  if list1 is None or list2 is None:
    return None

  temp1 = list1.head
  temp2 = list2.head
  s1 = set()
  intersect = LinkedList()
  
  while (temp1):
    s1.add(temp1.data)
    temp1 = temp1.next

  while temp2:
    if temp2.data in s1:
      intersect.add(temp2.data)
    temp2 = temp2.next

  return intersect


llist1 = LinkedList() 
llist1.push(700) 
llist1.push(758) 
llist1.push(30) 
llist1.push(70)
llist1.push(10)
llist1.push(38)
llist1.push(17)

llist2 = LinkedList() 
llist2.push(700) 
llist2.push(758) 
llist2.push(30) 
llist2.push(70)
llist2.push(10)
llist2.push(38)
llist2.push(17)

intersection(llist1,llist2).printlList()


      
    
