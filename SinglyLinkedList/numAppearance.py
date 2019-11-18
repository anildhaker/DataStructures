# number of times a given number appear in a linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None 

class LinkedList: 
  
    def __init__(self): 
        self.head = None
    
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node

    def numCount(self, num):
      temp = self.head
      count = 0
      while (temp):
        if temp.data == num:
          count += 1
        temp = temp.next
        
      return count 

llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(100) 
llist.push(2) 
llist.push(1)

print(llist.numCount(1))