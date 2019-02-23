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
    
    def pairwiseSwap(self):
      temp = self.head

      if temp is None:
        return
      while (temp is not None and temp.next is not None):
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next


llist = LinkedList()
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2)
llist.push(1)

llist.printList()
print
llist.pairwiseSwap()
llist.printList()