# finding intersection point of two linked lists

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
 
def intersectPoint(l1, l2):
  temp1 = l1
  temp2 = l2
  
  if temp1 is None or temp2 is None:
    return

  c1 = 0
  c2 = 0
  
  while temp1:
    c1 += 1
    temp1 = temp1.next
    
  while temp2:
    c2 += 1
    temp2 = temp2.next
    
  d = abs(c1 - c2)
  
  curr1 = l1
  curr2 = l2
  if c1 > c2:
    for i in range(d):
      curr1 = curr1.next
  else:
    for i in range(d):
      curr2 = curr2.next
      
  while curr1 and curr2:
    if curr1 == curr2:
      return curr1.data
      
    curr1 = curr1.next
    curr2 = curr2.next
    

head1 = Node(10)

head2 = Node(3)
  
newNode = Node(6)
head2.next = newNode; 
  
newNode = Node(9)
head2.next.next = newNode
  
newNode = Node(15) 
head1.next = newNode 
head2.next.next.next = newNode 

newNode = Node(30)  
head1.next.next = newNode 

head1.next.next.next = None

print(intersectPoint(head1,head2))