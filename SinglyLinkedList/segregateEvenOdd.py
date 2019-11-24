# Return a link list where all the even numbers appear before the odd ones.
# Input: 17->15->8->12->10->5->4->1->7->6->NULL
# Output: 8->12->10->4->6->17->15->5->1->7->NULL

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


  def evenOddSegregation(self):
    current = self.head
    oddHead = None
    evenHead = None
    lastEven = None 
    lastOdd = None

    while current:
      if current.data % 2 == 0:
        node = Node(current.data)
        if evenHead is None:
          evenHead = lastEven = node
        else:
          lastEven.next = node
          lastEven = lastEven.next

      else:
        node = Node(current.data)
        if oddHead is None:
          oddHead = lastOdd = node
        else:
          lastOdd.next = node
          lastOdd = lastOdd.next

      current = current.next
      
    lastEven.next = oddHead

    return evenHead
    

    
        

llist = LinkedList() 
llist.push(700) 
llist.push(758) 
llist.push(31) 
llist.push(70)
llist.push(11)
llist.push(38)
llist.push(17)

add = llist.evenOddSegregation()

while add is not None:
  print(add.data)
  add = add.next 