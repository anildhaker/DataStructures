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
            print(temp.data ,end = " ") 
            temp = temp.next
        

    def removeDuplicates(self):
      temp = self.head

      if temp is None:
        return
      
      while temp.next is not None:
        if (temp.data == temp.next.data):
          new = temp.next.next
          temp.next = None
          temp.next = new
        else:
          temp = temp.next
      return self.head

llist = LinkedList() # Here we are working with sorted linked List
llist.push(1) 
llist.push(2) 
llist.push(2) 
llist.push(3)
llist.push(3)
llist.push(4)
llist.push(4)

llist.printList()
llist.removeDuplicates()
print()
llist.printList()
print()
