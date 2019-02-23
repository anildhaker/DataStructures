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
    
    # using hash table to find the intersection of two linked lists.
    def intersectPoint(self, l1, l2):
      s = set()
      
      temp = l1.head
      while (temp):
        if (temp not in s):
          s.add(temp)
        temp = temp.next
      
      temp2 = l2.head
      while (temp2):
        if (temp2 in s):
          return temp2
        temp2 = temp2.next
        



l1 = LinkedList()
l1.push(5) 
l1.push(4) 
l1.push(3) 
l1.push(2)
l1.push(1)

l2 = LinkedList()
l2.push(7) 
l2.push(6) 
l2.push(8)
