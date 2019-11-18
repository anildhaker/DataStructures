# find Nth node from end
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

    def nthFromEnd(self, n):
      # trick is to find the len - n + 1 element from the beginning
      len = 0
      temp = self.head
      while temp:
        len += 1
        temp = temp.next
      
      if n > len:
        print("Index out of range")
        return
      
      temp = self.head
      for i in range(0, len - n):
        temp = temp.next

      print(temp.data)

llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(7) 
llist.push(20) 
llist.push(11)

llist.nthFromEnd(2)