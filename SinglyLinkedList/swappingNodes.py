# Swap two nodes without swapping the Data.
# we are assuming that all the keys are unique

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

# cases to be taken into account -
# 1. x or y may not present in list
# 2. x and y may or may not be adjacent
# 3. x or y are head nodes
# 4. x or y may be tail nodes

  def swapNodes(self, x, y):
    if x == y:
      return 
    # search for x
    currX = self.head
    prevX = None
    while (currX != None and currX.data != x):
        prevX = currX 
        currX = currX.next
      
    
    # search for x
    currY = self.head
    prevY = None
    while (currY != None and currY.data != y):
        prevY = currY
        currY = currY.next  
      
    # if x or y not present then Return
    if currX == None or currY == None:
      return
      
    # if x is not head node
    if prevX != None:
      prevX.next = currY
    else:
      self.head = currY

    # if y is not head node
    if prevY != None:
      prevY.next = currX
    else:
      self.head = currX

    # Swapping the pointers
    temp = currX.next
    currX.next = currY.next
    currY.next = temp
    
llist = LinkedList() 
llist.push(7) 
llist.push(70) 
llist.push(3) 
llist.push(77)
llist.push(11)
llist.push(39)
llist.push(100)

print('before swapping --')
llist.printlList()

llist.swapNodes(77,100)
print('after swapping--')
llist.printlList()
      
    