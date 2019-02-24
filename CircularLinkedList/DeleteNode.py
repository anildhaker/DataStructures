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
  
 
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print ("%d" %(temp.data),)
                temp = temp.next
                if (temp == self.head): 
                    break
    
    def deleteNode(self, key):
      cur = self.head
      prev = None

      if cur is None:
        return

      if(self.head.data == key and self.head.next == self.head):
        return None

      if (self.head.data == key):
        while (cur.next != self.head):
          prev = cur
          cur = cur.next
        cur.next = self.head.next
        self.head = cur
        return self.head
        

      while (cur.next != self.head):
        prev = cur
        cur = cur.next

        if (cur.data == key):
          prev.next = cur.next
          cur.next = None
          break
      return self.head
      
cllist = CircularLinkedList() 
  
cllist.push(40) 
cllist.push(30) 
cllist.push(20) 
cllist.push(10)

cllist.deleteNode(10)
cllist.printList()