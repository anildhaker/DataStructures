#Swap Nodes -- Without Swapping Data

class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None  

class LinkedList: 
  
    def __init__(self): 
        self.head = None
        self.counter = 0
  

    def push(self, new_data): 
  
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node

    def printList(self):  
        temp = self.head  
        while(temp):  
            print(temp.data ) 
            temp = temp.next

    def swapNodes(self, x, y):
      if x == y:
        return
      
      #Searching for Node x -- while keeping track of prevX and CurrX node
      prevX = None
      currX = self.head

      while (currX != None and currX.data != x):
        prevX = currX
        currX = currX.next
      
      prevY = None
      currY = self.head

      while (currY != None and currY.data != y):
        prevY = currY
        currY = currY.next

      if currX == None or currY == None:
        return
      
      # if x is not head node
      
      if prevX != None:
        prevX.next = currY
      else:
        self.head = currY

      if prevY != None:
        prevY.next = currX
      else:
        self.head = currX

      temp = currX.next
      currX.next = currY.next
      currY.next = temp 




llist = LinkedList()
llist.push(1) 
llist.push(2) 
llist.push(3) 
llist.push(4)
llist.push(5)

llist.printList()
print()
llist.swapNodes(3, 4)
print()
llist.printList()  