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

    def isCircular(self, list):  # Argument list can be a singly linked list or a circular list
      cur = self.head

      if cur is None:
        return
      while (cur.next):
        cur = cur.next
        if (cur.next == list.head):
          return True
      return False
        
    
cllist = CircularLinkedList() 
  

cllist.push(40) 
cllist.push(30) 
cllist.push(20) 
cllist.push(10)

print(cllist.isCircular(cllist))