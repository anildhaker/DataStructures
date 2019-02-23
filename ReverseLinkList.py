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
            print(temp.data)
            temp = temp.next
    
    def reverseLinkList(self):
      prev = None
      current = self.head
      while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
      self.head = prev



llist = LinkedList()
llist.push(1) 
llist.push(2) 
llist.push(3) 
llist.push(4)
llist.push(5)

llist.printList()
print
llist.reverseLinkList()
llist.printList()
