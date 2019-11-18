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

    def loopLength(self):
        slow = self.head
        fast = self.head
        
        while slow != fast:
          slow = slow.next
          fast = fast.next.next
          
        temp = slow
        count = 1
        slow = slow.next
        while temp != slow:
          count += 1
          slow = slow.next
          
        return count 

llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 

llist.head.next.next.next.next = llist.head;

print(llist.loopLength())
