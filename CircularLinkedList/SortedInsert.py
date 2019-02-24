class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList:
  
    def __init__(self): 
        self.head = None
  
    #insert Node at beginning
    def push(self, data): 
        new_node = Node(data) 
        temp = self.head 
          
        new_node.next = self.head 
  
        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = new_node 
  
        else: 
            new_node.next = new_node # For the first node 
  
        self.head = new_node  
  
    # Function to print nodes in a given circular linked list 
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ("%d" %(temp.data),)
                temp = temp.next
                if (temp == self.head): 
                    break
    
    def insertSort(self, new_node):
      cur = self.head
      if cur is None:
        new_node.next = new_node
        self.head = new_node

      elif (cur.data >= new_node.data):
        while (cur.next != self.head):
          cur = cur.next
        cur.next = new_node
        new_node.next = self.head
        self.head = new_node

      else:
        while (cur.next.data < new_node.data):
          cur = cur.next
          if (cur == self.head):
            break
        new_node.next = cur.next
        cur.next = new_node

  
  
# Driver program to test above function 
  
# Initialize list as empty 
cllist = CircularLinkedList() 
  
# Created linked list will be 11->2->56->12 
cllist.push(40) 
cllist.push(30) 
cllist.push(20) 
cllist.push(10)

x = Node(25)


cllist.printList()
print
cllist.insertSort(x)
cllist.printList() 